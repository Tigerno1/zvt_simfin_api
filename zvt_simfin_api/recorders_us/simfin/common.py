# -*- coding: utf-8 -*-

import simfin as sf 
from simfin.names import * 
import pandas as pd

from zvt.domain import ReportPeriod
from zvt.utils.time_utils import to_pd_timestamp
from zvt.contract.api import get_data
from zvt.domain_us.stock_meta_us import Stock 
from zvt.contract.recorder import Recorder, RecorderForEntities
from zvt.contract.api import get_data
from zvt.contract.api import df_to_db


class SimFinEntityRecorder(RecorderForEntities):

    provider = 'alphavantage'
    data_schema = Stock 
    entity_provider = 'alphavantage'
    entity_schema = Stock

    def __init__(self,
                 entity_type='stock',
                 exchanges=['NYSE', 'NASDAQ'],
                 entity_ids=None,
                 codes=None,
                 batch_size=10,
                 force_update=False,
                 sleeping_time=10) -> None:
        
        super().__init__(entity_type=entity_type,
                 exchanges=exchanges,
                 entity_ids=entity_ids,
                 codes=codes,
                 batch_size=batch_size,
                 force_update=force_update,
                 sleeping_time=sleeping_time)
                 

class BaseSimFinFinanceRecorder(Recorder):

    refresh_days = 3
    sf.set_data_dir('~/simfin_data/')
    sf.set_api_key(api_key='') # api key for simfin

    def get_data_from_simfin(self): 
        if self.datasets:
            for dataset in self.datasets:
                df = sf.load(dataset=dataset, variant=self.variant, market=self.market, refresh_days=self.refresh_days)
                yield dataset, df


    def get_data_map(self):
        raise NotImplementedError

    def get_seasons(self, season):
        if season == 'Q1':
            return ReportPeriod.season1.value
        if season == 'Q2':
            return ReportPeriod.season2.value
        if season == 'Q3':
            return ReportPeriod.season3.value
        if season == 'Q4':
            return ReportPeriod.season4.value 
    
    def drop_columns(self, df):
        df.drop(columns=['SimFinId', 'Currency', 'Fiscal Year', 'Fiscal Period', 'Source', 'Restated Date', 'Publish Date'], inplace=True)
        return df

    def run(self):
        data_map = self.get_data_map()
        for dataset, df in self.get_data_from_simfin():
            df.dropna(subset=['Ticker'])
            codes = set(df['Ticker'].to_list())
            code_dict = {}
            for code in codes:
                try:
                    s = SimFinEntityRecorder(codes = [code])
                    code_dict.update({s.entities[0].code: s.entities[0].exchange})
                except Exception as e:
                    self.logger.warning(f"Index Error: {code}: {e}")
                    continue
            df_ex = pd.DataFrame.from_dict(code_dict, orient='index', columns=['exchange'])

            df = pd.merge(df, df_ex, how="left", left_on='Ticker', right_on=df_ex.index)
            df['report_period'] = df['Fiscal Period'].apply(lambda x: self.get_seasons(x))
            df['timestamp'] = df['Publish Date'].apply(lambda x: to_pd_timestamp(x))
            df['restated_date'] = df['Restated Date'].apply(lambda x: to_pd_timestamp(x))
            df['entity_type'] = 'stock'
            df['provider'] = self.provider
            df['entity_id'] = df[['entity_type', 'exchange', 'Ticker']].apply(lambda x: '_'.join(x.astype(str)), axis=1)
            df['id'] = df[['entity_id', 'Publish Date']].apply(lambda x: '_'.join(x.astype(str)), axis=1)

            df = self.drop_columns(df)
            df.rename(columns=data_map, inplace=True)
            
            df = df.drop_duplicates(subset=('id'), keep='last')
            df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=False)
            self.logger.info(df.tail())
            self.logger.info(f"persist {dataset}, market: {self.market}, variant: {self.variant} successs")

class BaseSimFinValuationRecorder(BaseSimFinFinanceRecorder):
    
    
    def get_data_from_simfin(self): 
        if self.datasets:
            for dataset in self.datasets:
                df = sf.load(dataset=dataset, variant=self.variant, market=self.market, refresh_days=self.refresh_days)
                yield dataset, df

    def drop_columns(self, df):
        df.drop(columns=['SimFinId', 'Date'], inplace=True)
        return df
    

    def run(self):
        data_map = self.get_data_map()
        for dataset, df in self.get_data_from_simfin():
            df = df.reset_index()
            df.dropna(subset=['Ticker'])
            codes = set(df['Ticker'].to_list())
            code_dict = {}
            for code in codes:
                try:
                    s = SimFinEntityRecorder(codes = [code])
                    code_dict.update({s.entities[0].code: (s.entities[0].name, s.entities[0].exchange)})
                except Exception as e:
                    self.logger.warning(f"Index Error: {code}: {e}")
                    continue

            df_ex = pd.DataFrame.from_dict(code_dict, orient='index', columns=['name', 'exchange'])

            df = pd.merge(df, df_ex, how="left", left_on='Ticker', right_on=df_ex.index)

            df['timestamp'] = df['Date'].apply(lambda x: to_pd_timestamp(x))

            df['entity_type'] = 'stock'
            df['provider'] = self.provider
            df['entity_id'] = df[['entity_type', 'exchange', 'Ticker']].apply(lambda x: '_'.join(x.astype(str)), axis=1)
            df['id'] = df[['entity_id', 'Date']].apply(lambda x: '_'.join(x.astype(str)), axis=1)
            if dataset == 'shareprices':
                df['level'] = '1d'

            df = self.drop_columns(df)
            df.rename(columns=data_map, inplace=True)

            df = df.drop_duplicates(subset=('id'), keep='last')
            df_to_db(df=df, data_schema=self.data_schema, provider=self.provider, force_update=False)
            self.logger.info(df.tail())
            self.logger.info(f"persist valuation data, market: {self.market}, variant: {self.variant} successs")


if __name__ == '__main__':
    BaseSimFinEntityRecorder().run()

    
    