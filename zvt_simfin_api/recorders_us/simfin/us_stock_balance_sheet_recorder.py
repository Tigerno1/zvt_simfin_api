from zvt.recorders_us.simfin.common import BaseSimFinFinanceRecorder
from zvt.domain_us.finance_us import BalanceSheet

balance_sheet_map = {
    "Ticker": "code",
    "Report Date": "report_date",
    'Restated Date': "restated_date",
    "Shares (Basic)": "basic_shares",
    "Shares (Diluted)": "deluted_shares",
    "Cash, Cash Equivalents & Short Term Investments": "cash_short_investment", 
    "Cash & Cash Equivalents": "cash_cash_equivalents", 
    "Short Term Investments": "short_investments",	
    
    "Accounts & Notes Receivable": "accounts_notes_receivable", 
    "Accounts Receivable, Net": "accounts_receivable", 
    "Notes Receivable, Net": "notes_receivable",
    "Unbilled Revenues": "unbilled_revenues",
    
    "Inventories": "inventories", 
    "Raw Materials": "raw_materials",  
    "Work In Process": "work_in_process", 
    "Finished Goods": "finished_goods",
    "Other Inventory": "other_inventory", 	
    
    "Other Short Term Assets": "other_short_assets", 
    "Prepaid Expenses": "prepaid_expenses", 
    "Derivative & Hedging Assets (Short Term)": "short_derivative_hedging_assets", 
    "Assets Held-for-Sale":	"assets_held_for_sale",
    "Deferred Tax Assets (Short Term)": "short_deferred_tax_assets",
    "Income Taxes Receivable": "income_taxes_receivable",
    "Discontinued Operations (Short Term)": "short_discontinued_operations",
    "Misc. Short Term Assets": "misc_short_assets", 
    
    "Total Current Assets":	"total_current_assets",
    
    "Property, Plant & Equipment, Net": "net_property_plant_equipment", 
    "Property, Plant & Equipment": "property_plant_equipment",
    "Accumulated Depreciation":	"accumulated_depreciation",
    
    "Long Term Investments & Receivables":"long_investments_receivables",
    "Long Term Investments": "long_investments",
    "Long Term Marketable Securities": "long_marketable_securities",
    "Long Term Receivables": "long_receivables",
    
    "Other Long Term Assets": "other_long_assets",  
    "Intangible Assets": "intangible_assets",
    "Goodwill": "goodwill",
    "Other Intangible Assets": "other_intangible_assets",	
    "Prepaid Expense": "prepaid_expenses",
    "Deferred Tax Assets (Long Term)": "long_deferred_tax_assets", 
    "Derivative & Hedging Assets (Long Term)": "long_derivative_hedging_assets",
    "Prepaid Pension Costs": "prepaid_pension_costs", 
    "Discontinued Operations (Long Term)": "long_discontinued_operation", 
    "Investments in Affiliates": "investment_affiliates",
    "Misc. Long Term Assets": "misc_long_assets",
    
    "Total Noncurrent Assets": "total_noncurrent_assets", 
    "Total Assets":	"total_assets", 
    
    "Payables & Accruals": "payables_accruals",
    "Accounts Payable": "accounts_payable",
    "Accrued Taxes": "accrued_taxes", 
    "Interest & Dividends Payable":	"interest_dividends_payable",
    "Other Payables & Accruals": "other_payables_accruals",
    
    "Short Term Debt": "short_debt", 
    "Short Term Borrowings": "short_borrowings", 
    "Short Term Capital Leases": "short_capital_leases", 
    "Current Portion of Long Term Debt": "current_portion_of_long_debt", 
    
    "Other Short Term Liabilities": "other_short_liabilities", 
    "Deferred Revenue (Short Term)": "short_deferred_revenue", 
    "Liabilities from Derivatives & Hedging (Short Term)": "short_liabilities_derivatives_hedging", 
    "Deferred Tax Liabilities (Short Term)": "short_deferred_tax_liabilities", 
    "Liabilities from Discontinued Operations (Short Term)": "short_liabilities_discountinued_operations",
    "Misc. Short Term Liabilities":	"misc_short_liabilities",
    
    "Total Current Liabilities": "total_current_liabilities", 
    
    "Long Term Debt": "long_debt",
    "Long Term Borrowings": "long_borrowings",
    "Long Term Capital Leases":	"long_capital_leases",
    
    "Other Long Term Liabilities": "other_long_liabilities", 
    "Accrued Liabilities": "accrued_liabilities", 
    "Pension Liabilities": "pension_liabilities", 
    "Pensions":	"pensions",
    "Other Post-Retirement Benefits": "other_postretirement_benefits",  
    "Deferred Compensation": "deferred_compensation", 
    "Deferred Revenue (Long Term)":	"long_deferred_revenue", 
    "Deferred Tax Liabilities (Long Term)": "long_deferred_tax_liabilities", 
    "Liabilities from Derivatives & Hedging (Long Term)": "long_liabilities_derivatives_hedging", 
    "Liabilities from Discontinued Operations (Long Term)": "long_liabilities_discountinued_operations", 
    "Misc. Long Term Liabilities": "misc_long_liabilities", 
    
    "Total Noncurrent Liabilities": "total_noncurrent_liabilities", 
    "Total Liabilities": "total_liabilities", 
    
    "Preferred Equity": "preferred_equity", 
    "Share Capital & Additional Paid-In Capital": "share_capial_additional_paidin_capital",	
    "Common Stock": "common_stock", 
    "Additional Paid in Capital": "additional_paidin_capital", 
    "Other Share Capital": "other_share_capital",

    "Treasury Stock": "treasury_stock", 
    "Retained Earnings": "retained_earnings", 
    "Other Equity": "other_equity", 
	
    "Equity Before Minority Interest": "equity_before_minority_interest", 
    "Minority Interest": "minority_interest", 
    "Total Equity": "total_equity", 
    "Total Liabilities & Equity": "total_liabilities_equity", 

    "Interbank Assets": "fi_interbank_Assets", 
    "Fed Funds Sold & Repos": "fi_fed_funds_sold_Repos", 
    "Other Interbank Assets": "fi_other_interbank_assets", 

    "Short & Long Term Investments": "fi_short_long_investments", 
    "Trading Securities": "fi_trading_securities", 
    "Investment Securities Available for Sale": "fi_investment_securities_available_for_sale", 
    "Investment Securities Held to Maturity": "fi_investment_securities_held_to_maturity", 
    "Real Estate Investments": "fi_real_estate_investments", 
    "Other Investments": "fi_other_investments",
    
    
    "Net Loans": "fi_net_loans", 
    "Reserve for Loan Losses": "fi_reserve_for_loan_losses", 
    "Total Loans": "fi_total_loans", 
    
    
    "Total Commercial Loans": "fi_total_commercial_loans", 
    "Commercial Real Estate Loans":	"fi_commercial_real_estate_loans", 
    "Other Commercial Loans": "fi_other_coummercial_loans", 	
    
    "Total Consumer Loans": "fi_total_consumer_loans", 
    "Credit Card Loans": "fi_credit_card_loans", 
    "Home Equity Loans": "fi_home_equity_loans", 
    "Family Residential Loans": "fi_family_residential_loans", 
    "Auto Loans": "fi_auto_loans", 
    "Student Loans": "fi_student_loans", 
    "Other Consumer Loans": "fi_other_consumer_loans", 

    "Other Loans": "fi_other_loans", 

    "Net Fixed Assets": "fi_net_fixed_assets", 
    "Operating Lease Assets": "fi_operating_lease_assets", 
    "Other Fixed Assets": "fi_other_fixed_assets", 
    
    "Derivatives & Hedging (Assets)": "fi_derivatives_hedging_assets",
    "Discontinued Operations (Assets)": "fi_discontinued_operations_assets", 
    "Customer Acceptances & Liabilities": "fi_customer_acceptances_liabilities", 	
    
    "Other Assets": "fi_other_assets",
    
    "Total Deposits": "fi_total_deposits", 
    "Demand Deposits": "fi_demand_deposits", 
    "Interest Bearing Deposits": "fi_interest_bearing_deposits", 
    "Saving Deposits": "fi_saving_deposits", 
    "Time Deposits": "fi_time_deposits", 
    "Other Deposits": "fi_other_deposits", 
    
    "Securities Sold Under Repo": "fi_securities_sold_under_repo", 
    "Trading Account Liabilities": "fi_trading_account_liabilities", 
    "Payables Broker Dealers": "fi_payables_broker_dealers", 

    "Derivatives & Hedging (Liabilities)": "fi_derivatives_hedging_liabilities", 
    "Discontinued Operations (Liabilities)": "fi_discontinued_operations_liabilities", 

    "Total Investments": "fi_total_investments", 
    "Fixed Income-Trading/AFS & Short Term Inv.": "fi_fixed_income_trading_AFS_short_investment", 
    "Loans & Mortgages": "fi_loans_mortgages", 
    "Fixed Income Securities HTM": "fi_fixed_income_securities_HTM", 
    "Equity Securities": "fi_equity_securities", 
    "Real Estate Investments": "fi_real_estate_investments", 
    "Other Investments": "fi_other_investments",

    "Deferred Policy Acquisition Costs": "fi_deferred_policy_aquisition_costs", 

    "Insurance Reserves": "fi_insurance_reserves", 
    "Reserve for Outstanding Claims & Losses": "fi_reserve_outstanding_claims_losses", 
    "Premium Reserve (Unearned)": "fi_unearned_premium_reserve", 
    "Life Policy Benefits":	"fi_life_policy_benefits", 
    "Other Insurance Reserves": "fi_other_insurance_reserves", 
    
    "Funds for Future Appropriations": "fi_funds_future_appropriation"

}

class USStockBalanceSheetRecorder(BaseSimFinFinanceRecorder):
    provider = "simfin"
    data_schema = BalanceSheet
    
    datasets = ["balance", "balance-banks", 'balance-insurance']
    market = "us"
    variant = "quarterly-full"

    def get_data_map(self):
        return balance_sheet_map


__all__ = ['USStockBalanceSheetRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStockBalanceSheetRecorder()
    recorder.run()

    