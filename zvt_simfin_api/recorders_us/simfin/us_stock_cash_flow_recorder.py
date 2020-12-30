from zvt.recorders_us.simfin.common import BaseSimFinFinanceRecorder
from zvt.domain_us.finance_us import CashFlowStatement

cash_flow_map = {
    "Ticker": "code",
    "Report Date": "report_date",
    'Restated Date': "restated_date",
    "Shares (Basic)": "basic_shares",
    "Shares (Diluted)": "deluted_shares",
    
    "Net Income/Starting Line" : "net_income_starting_line",
    "Net Income": "net_income",
    "Net Income from Discontinued Operations": "net_income_discontinued_operations",
    "Other Adjustments": "other_adjustments",
    "Depreciation & Amortization": "depreciation_amortization",
    "Non-Cash Items": "noncash_items",
    "Stock-Based Compensation": "stockbased_compensation",
    "Deferred Income Taxes": "deferred_income_taxes",
    "Other Non-Cash Adjustments": "other_noncash_adjustments",
    "Change in Working Capital": "change_working_capital",
    "Change in Accounts Receivable": "change_accounts_payable",
    "Change in Inventories": "change_inventories",
    "Change in Accounts Payable": "change_accounts_payable",	
    "Change in Other": "change_other", 	
    "Net Cash from Discontinued Operations (Operating)": "operating_net_cash_discontinued_operation",
    "Net Cash from Operating Activities": "net_cash_operation_activities",
    "Change in Fixed Assets & Intangibles":	"change_fiexed_assets_intangibles",
    "Disposition of Fixed Assets & Intangibles": "disposition_fixed_assets_intangibles",	
    "Disposition of Fixed Assets": "disposition_fixed_assets",
    "Disposition of Intangible Assets":	"disposition_intangible_assets",
    "Acquisition of Fixed Assets & Intangibles": "acquisition_fixed_assets_intangibles",	
    "Purchase of Fixed Assets":	"purchase_fixed_assets",
    "Acquisition of Intangible Assets":	"acquisition_intangible_assets",
    "Other Change in Fixed Assets & Intangibles": "other_change_fixed_assets_intangibles",
    "Net Change in Long Term Investment": "net_change_long_investment",
    "Decrease in Long Term Investment":	"decrease_long_investment",
    "Increase in Long Term Investment":	"increase_long_investment",
    "Net Cash from Acquisitions & Divestitures": "net_cash_acquisitions_divestitures",
    "Net Cash from Divestitures": "net_cash_divestitures",
    "Cash for Acquisition of Subsidiaries":	"cash_acquisition_subsidiaries",
    "Cash for Joint Ventures": "cash_joint_ventures",
    "Net Cash from Other Acquisitions": "net_cash_other_aquisitions",	
    "Other Investing Activities": "other_investing_activities",	
    "Net Cash from Discontinued Operations (Investing)": "investing_net_cash_discontinued_operation",	
    "Net Cash from Investing Activities": "net_cash_investing_activites",
    "Dividends Paid": "dividends_paid",
    "Cash from (Repayment of) Debt": "cash_repayment_debt",	
    "Cash from (Repayment of) Short Term Debt, Net": "net_cash_repayment_short_debt",	
    "Cash from (Repayment of) Long Term Debt, Net": "net_cash_repayment_long_debt",	
    "Repayments of Long Term Debt": "repayments_long_debt",	
    "Cash from Long Term Debt": "cash_long_debt",	
    "Cash from (Repurchase of) Equity": "cash_repurchase_equity",	
    "Increase in Capital Stock": "increase_capital_stock",
    "Decrease in Capital Stock": "decrease_capital_stock",	
    "Other Financing Activities": "other_financing_activities",
    "Net Cash from Discontinued Operations (Financing)": "financing_net_cash_discontinued_operation",	
    "Net Cash from Financing Activities": "net_cash_financing_activities",	
    "Net Cash Before Disc. Operations and FX": 	"net_cash_before_disc_operations_fx",
    "Change in Cash from Disc. Operations and Other": "change_cash_disc_operations_other",
    "Net Cash Before FX": "net_cash_before_fx",
    "Effect of Foreign Exchange Rates": "effect_foreign_exchange_rates",	
    "Net Change in Cash": "net_change_cash",

    'Net Change in Operating Loans': "fi_net_change_operating_loans", 
    'Increase in HTM Investments': "fi_increase_htm_investments", 
    'Net Change in Customer Loans': "fi_net_change_customer_loans", 
    'Accrued Interest Receivable': "fi_accrued_interest_payable", 
    'Net Change of Interbank Liabilities': "fi_net_change_interbank_liabilities", 
    'Net Change of Investments': "fi_net_change_of_investments", 
    'Trading Assets & Liabilities': "fi_trading_assets_liabilities", 
    'Net Change in Interbank Transfers': "fi_net_change_interbank_transfers", 
    'Decrease in HTM Investments': "fi_decrease_htm_investments", 
    'Gain On Sale of Securities & Loans': "fi_gain_sales_securities_loans", 
    'Increase in AFS Investments': "fi_increase_afs_investments", 
    'Decrease in Investments': "fi_decrease_investments", 
    'Net Change in Interbank Assets': "fi_net_change_interbank_assets", 
    'Other Operating Assets/Liabilities': "fi_other_operating_assets_liabilities", 
    'Net Change in Other Investments': "fi_net_change_other_investments", 
    'Net Change in Loans & Interbank': "net_change_loans_interbank", 
    'Net Change In Deposits': "fi_net_change_deposits", 
    'Net Change in Other Loans': "fi_net_change_other_loans", 
    'Accrued Interest Payable': "fi_accrued_interest_payable", 
    'Decrease in AFS Investments': "fi_decrease_afs_investments", 
    'Provision for Loan Losses': "fi_provision_loan_losses", 
    'Capital Expenditures': "fi_capital_expenditure", 
    'Net Change in Investments': "fi_net_change_in_investments", 
    'Net Change of Interbank Assets': "fi_net_change_interbank_assets", 
    'Increase in Investments': "fi_increase_investments",
    
    'Change in Insurance Reserves': "fi_change_insurance_recerves"
}

class USStockCashFlowRecorder(BaseSimFinFinanceRecorder):
    provider = "simfin"
    data_schema = CashFlowStatement
    
    datasets = ["cashflow", "cashflow-banks", 'cashflow-insurance']
    market = "us"
    variant = "quarterly-full"

    def get_data_map(self):
        return cash_flow_map


__all__ = ['USStockCashFlowRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStockCashFlowRecorder()
    recorder.run()

    