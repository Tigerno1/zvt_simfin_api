from zvt.recorders_us.simfin.common import BaseSimFinValuationRecorder
from zvt.domain_us.valuation_us import StockValuation

stock_valuation_map = {
    "Ticker": "code",
    
    "Market-Cap": "market_cap",	
    "Price to Earnings Ratio (quarterly)": "pe_q",	
    "Price to Earnings Ratio (ttm)": "pe_ttm",	
    "Price to Sales Ratio (quarterly)": "ps_q",	
    "Price to Sales Ratio (ttm)": "ps_ttm",	
    "Price to Book Value": "pb",	
    "Price to Free Cash Flow (quarterly)": "pcf_q",	
    "Price to Free Cash Flow (ttm)": "pcf_ttm",	
    "Enterprise Value": "ev",	
    "EV/EBITDA": "ev_ebitda",	
    "EV/Sales": "ev_sales",	
    "EV/FCF": "ev_fcf",	
    "Book to Market Value": "book_market",	
    "Operating Income/EV": "operating_income_ev"
}

class USStockValuationRecorder(BaseSimFinValuationRecorder):
    provider = "simfin"
    data_schema = StockValuation
    
    datasets = ["derived-shareprices"]
    market = "us"
    variant = "daily"

    def get_data_map(self):
        return stock_valuation_map


__all__ = ['USStockValuationRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStockValuationRecorder()
    recorder.run()

    