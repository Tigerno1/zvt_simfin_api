from zvt.recorders_us.simfin.common import BaseSimFinValuationRecorder
from zvt.domain_us.stock_1d_kdata_us import USStock1dKdata

stock_1d_kdata_map = {
    "Ticker": "code",
    'Open': "open",	
    'Low': "low",	
    'High': "high",	
    'Close': "close",
    'Adj. Close': "adj_close",	
    'Dividend': "dividend",	
    'Volume': "volume",	
    'Shares Outstanding': "shares_outstanding",
}

class USStock1DKdataRecorder(BaseSimFinValuationRecorder):
    provider = "simfin"
    data_schema = USStock1dKdata
    
    datasets = ["shareprices"]
    market = "us"
    variant = "latest"

    def get_data_map(self):
        return stock_1d_kdata_map


__all__ = ['USStock1DKdataRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStock1DKdataRecorder()
    recorder.variant = 'full'
    recorder.run()