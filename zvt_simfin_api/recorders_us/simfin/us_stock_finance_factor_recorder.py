from zvt.recorders_us.simfin.common import BaseSimFinFinanceRecorder
from zvt.domain_us.finance_us import FinanceFactor

finance_factor_map = {
    "Ticker": "code",
    "Report Date": "report_date",
    'Restated Date': "restated_date",
    "Shares (Basic)": "basic_shares",
    "Shares (Diluted)": "deluted_shares",
    
    "EBITDA": "ebitda",
    "Total Debt": "total_debt",
    "Free Cash Flow": "fcf",
    "Gross Profit Margin": "gross_profit_margin",
    "Operating Margin": "operating_margin",	
    "Net Profit Margin": "net_profit_margin",
    "Return on Equity": "roe",	
    "Return on Assets": "roa",	
    "Free Cash Flow to Net Income": "fcf_net_income",	
    "Current Ratio": "current_ratio",	
    "Liabilities to Equity Ratio": "liabilities_to_equity_ratio",	
    "Debt Ratio": "debt_ratio",	
    "Earnings Per Share, Basic": "basic_eps",	
    "Earnings Per Share, Diluted": "diluted_esp",
    "Sales Per Share": "sps",	
    "Equity Per Share": "equity_ps",	
    "Free Cash Flow Per Share": "fcf_ps",	
    "Dividends Per Share":"dps",	
    "Pietroski F-Score": "pietroski"
}

class USStockFinanceFactorRecorder(BaseSimFinFinanceRecorder):
    provider = "simfin"
    data_schema = FinanceFactor
    
    datasets = ["derived", "derived-banks", "derived-insurancec"]
    market = "us"
    variant = "annual"

    def get_data_map(self):
        return finance_factor_map
    
    def drop_columns(self, df):
        df.drop(columns=['SimFinId', 'Currency', 'Fiscal Year', 'Fiscal Period', 'Restated Date', 'Publish Date'], inplace=True)
        return df
    


__all__ = ['USStockFinanceFactorRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStockFinanceFactorRecorder()
    recorder.run()

    