from zvt.recorders_us.simfin.common import BaseSimFinDataRecorder
from zvt.domain_us.finance_us import IncomeStatement

income_statement_map = {
    "Ticker": "code",
    "Report Date": "report_date",
    'Restated Date': "restated_date",
    "Shares (Basic)": "basic_shares",
    "Shares (Diluted)": "deluted_shares",
    
    "Revenue": "revenue",
    "Sales & Services Revenue": "sales_services_revenue",
    "Financing Revenue": "financing_revenue",
    "Other Revenue": "other_revenue",
    "Cost of Revenue": "cost_revenue",
    "Cost of Goods & Services": "cost_goods_services",
    "Cost of Financing Revenue": "cost_financing_revenue",
    "Cost of Other Revenue": "cost_other_revenue",
    "Gross Profit": "gross_profit",
    "Other Operating Income": "other_operating_income",
    "Operating Expenses": "operating_expenses",
    "Selling, General & Administrative": "selling_general_administrative",
    "Selling & Marketing": "selling_marketing	",
    "General & Administrative": "general_administrative",
    "Research & Development": "research_development",
    "Depreciation & Amortization": "depreciation_amortization",
    "Provision for Doubtful Accounts": "provision_doubtful_accounts",
    "Other Operating Expenses": "other_operating_expenses",
    "Operating Income (Loss)": "operating_income",
    "Non-Operating Income (Loss)": "nonoperating_income",
    "Interest Expense, Net": "net_interest_expense",
    "Interest Expense": "interest_expense",
    "Interest Income": "interest_income",
    "Other Investment Income (Loss)": "other_investment_income",
    "Foreign Exchange Gain (Loss)": "foreign_exchange_gain",
    "Income (Loss) from Affiliates": "income_from_affliates",
    "Other Non-Operating Income (Loss)": "other_nonoperating_income",
    "Pretax Income (Loss), Adj.": "adj_pretax_income",
    "Abnormal Gains (Losses)": "abnormal_gains",
    "Acquired In-Process R&D": "acquired_inprocess_R_D",
    "Merger & Acquisition Expense": "merger_acquisition_expense",
    "Abnormal Derivatives": "abnormal_derivatives",
    "Disposal of Assets": "disposal_assets",
    "Early Extinguishment of Debt": "early_extinguishment_debt",
    "Asset Write-Down": "asset_writedown",
    "Impairment of Goodwill & Intangibles": "impairment_goodwill_intangibles",
    "Sale of Business": "sale_bueinsess",
    "Legal Settlement": "legal_settlement",
    "Restructuring Charges": "restructuring_charges ",
    "Sale of Investments & Unrealized Investments": "sales_investments_unrealized_investments",
    "Insurance Settlement": "insurance_settlement",
    "Other Abnormal Items": "other_abnormal_items ",
    "Pretax Income (Loss)": "pretax_income",
    "Income Tax (Expense) Benefit, Net": "net_income_tax_benefit",
    "Current Income Tax": "current_income_tax",
    "Deferred Income Tax": "deferred_income_tax",
    "Tax Allowance/Credit": "tax_allowance_credit",
    "Income (Loss) from Affiliates, Net of Taxes": "income_affliates_net_taxes",
    "Income (Loss) from Continuing Operations": "income_continuing_operations",
    "Net Extraordinary Gains (Losses)": "net_extraordinary_gains",
    "Discontinued Operations": "discontinued_operations	",
    "Accounting Charges & Other": "accounting_charges_other",
    "Income (Loss) Incl. Minority Interest": "income_incl_minority_interest",
    "Minority Interest": "minority_interest",
    "Net Income": "net_income",
    "Preferred Dividends": "preferred_dividends",
    "Other Adjustments": "other_adjustments",
    "Net Income (Common)": "net_common_income",
    
    'Trading Account Profits/Losses': "fi_trading_account_profits_losses", 
    'Debt Valuation Adjustment': "fi_debt_valuation_adjustment", 
    'Commissions & Fees Paid': "fi_commissions_fee_paid", 
    'Net Interest Income': "fi_net_interest_income", 
    'Investment Income (Loss)': "investment_income", 
    'Other Non-Interest Income': "fi_other_noninterest_income", 
    'Total Interest Income': "fi_total_interest_income", 
    'Total Non-Interest Expense': "fi_total_noninterest_expense", 
    'Total Non-Interest Income': "fi_total_noninterest_income", 
    'Net Revenue after Provisions': "fi_net_revenue_after_provisions", 
    'Commissions & Fees Earned': "fi_commissions_fee_earned", 
    'Provision for Loan Losses': "fi_provision_loan_losses", 
    'Net OTTI Losses Recognised in Earnings': "fi_net_otti_losses_recognised_earnings", 
    'Total Interest Expense': "fi_total_interest_expense", 
    'Credit Valuation Adjustment': "fi_credit_valuation_adjustment", 
    'Sale of Loan Income (Loss)': "fi_sale_loan_income",

    'Total Claims & Losses': "fi_total_claims_losses", 
    'Net Premiums Earned': "fi_net_preminums_earned", 
    'Foreign Exchange': "fi_foreign_exchange", 
    'Total OTTI Realized': "fi_total_otti_realized", 
    'Income from Real Estate': "fi_income_real_estate", 
    'Policy Charges & Fees': "fi_policy_charges_fees", 
    'Other Realized Investment Gains': "fi_other_realized_investment_gains", 
    'Long Term Charges': "fi_long_charges", 
    'Total Realized Investment Gains': "fi_total_realized_investment_gains", 
    'Underwriting Expense & Acquisition Cost': "fi_underwriting_expense_aquisition_cost", 
    'Claims & Losses': "fi_claims_losses", 
    'Other Income': "fi_other_income", 
    'Net Investment Losses': "fi_net_investment_loss", 
    'Other Claims & Losses': "fi_other_claims_losses"
}

class USStockIncomeStatementRecorder(BaseSimFinDataRecorder):
    provider = "simfin"
    data_schema = IncomeStatement
    
    datasets = ["income", "income-banks", 'income-insurance']
    market = "us"
    variant = "quarterly-full"

    def get_data_map(self):
        return income_statement_map


__all__ = ['USStockIncomeStatementRecorder']

if __name__ == '__main__':
    # init_log('blance_sheet.log')
    recorder = USStockIncomeStatementRecorder()
    recorder.run()

    