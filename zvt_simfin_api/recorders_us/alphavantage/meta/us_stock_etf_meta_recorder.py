# -*- coding: utf-8 -*-

import io

import pandas as pd
import requests

from zvt.contract.api import df_to_db
from zvt.contract.recorder import Recorder
from zvt.utils.time_utils import to_pd_timestamp
from zvt.domain_us import Stock, StockDetail, Etf, StockIndustry
from zvt.recorders_us.alphavantage.common import ApiWrapper

class AlphaVantageUSStockListRecorder(Recorder):
    data_schema = Stock 
    provider = 'alphavantage'
    api_wrapper = ApiWrapper()

    def run(self):
        resp = self.api_wrapper.request(function="LISTING_STATUS")
        self.identify_asset_type(resp, "active")
        resp = self.api_wrapper.request(function="LISTING_STATUS", state="delisted")
        self.identify_asset_type(resp, "delisted")

    def identify_asset_type(self, response, status):
        df = pd.read_csv(io.BytesIO(response.content), encoding='utf-8', dtype=str, parse_dates=['ipoDate'])

        if df is not None:
            # df = df[['symbol', 'name', 'exchange', 'assetType', 'ipoDate', 'delistingDate']]
            stock = df[df['assetType'] == 'Stock'].copy()

            self.clean_and_store_data("stock", stock, status)

            etf = df[df['assetType'] == 'ETF'].copy()

            self.clean_and_store_data('etf', etf, status)

    def clean_and_store_data(self, type_, df, status):
        df.dropna(subset=['symbol'])
        df.columns = ['code', 'name', 'exchange', 'entity_type', 'list_date', 'end_date', 'status']
        df['list_date'] = df['list_date'].apply(lambda x: to_pd_timestamp(x))
        df['end_date'] = df['end_date'].apply(lambda x: to_pd_timestamp(x))
        df['id'] = df[['entity_type', 'exchange', 'code']].apply(lambda x: '_'.join(x.astype(str)), axis=1)
        df['entity_id'] = df['id']
        df['timestamp'] = df['list_date']
        df = df.drop_duplicates(subset=('id'), keep='last')
        if type_ == 'stock':
            df_to_db(df=df, data_schema=Stock, provider=self.provider, force_update=False)
        # persist StockDetail too
            df_to_db(df=df, data_schema=StockDetail, provider=self.provider, force_update=False)
            df_to_db(df=df, data_schema=StockIndustry, provider=self.provider, force_update=False) 
        if type_ == 'etf':
            df_to_db(df=df, data_schema=Etf, provider=self.provider, force_update=False)
        self.logger.info(df.tail())
        self.logger.info(f"persist {status} {type_} list successs")


__all__ = ['AlphaVantageUSStockListRecorder']

if __name__ == '__main__':
    spider = AlphaVantageUSStockListRecorder()
    spider.run()
