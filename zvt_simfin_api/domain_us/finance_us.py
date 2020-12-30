# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import Mixin
from zvt.contract.register import register_schema

FinanceBase = declarative_base()


class BalanceSheet(FinanceBase, Mixin):

    @classmethod
    def important_cols(cls):
        return ['total_assets', 'total_liabilities', 'equity', 'cash_and_cash_equivalents', 'accounts_receivable',
                'inventories', 'goodwill']

    __tablename__ = 'balance_sheet'

    provider = Column(String(length=32))
    code = Column(String(length=32))

    report_period = Column(String(length=32))
    report_date = Column(DateTime)
    restated_date = Column(DateTime)

    # Shares (Basic)	Shares (Diluted)
    basic_shares = Column(Float)
    deluted_shares = Column(Float)

    # Asset
    
    # Cash Equivalents & Short Term Investments	
    cash_short_investment = Column(Float)
        # Cash & Cash Equivalents
    cash_cash_equivalents = Column(Float)
        # Short Term Investments
    short_investments = Column(Float)	
    
    # Accounts & Notes Receivable	
    accounts_notes_receivable = Column(Float)
        # Accounts Receivable, Net
    accounts_receivable = Column(Float)
        # Notes Receivable, Net 
    notes_receivable = Column(Float)
        # Net Unbilled Revenues
    unbilled_revenues = Column(Float)
    
    # Inventories	
    inventories = Column(Float)
        # Raw Materials	
    raw_materials = Column(Float)
        # Work In Process	
    work_in_process = Column(Float)
        # Finished Goods 
    finished_goods = Column(Float)
        # Other Inventory
    other_inventory = Column(Float)	
    
    # Other Short Term Assets
    other_short_assets = Column(Float)
        # Prepaid Expenses	
    prepaid_expenses = Column(Float)
        # Derivative & Hedging Assets (Short Term)
    short_derivative_hedging_assets = Column(Float)
        # Assets Held-for-Sale	
    assets_held_for_sale = Column(Float)
        # Deferred Tax Assets (Short Term)
    short_deffered_tax_assets = Column(Float)
        # Income Taxes Receivable 
    income_taxes_receivable = Column(Float)
        # Discontinued Operations (Short Term)	
    short_discountiued_operations = Column(Float)
        # Misc. Short Term Assets
    misc_short_assets = Column(Float)
    
    # Total Current Assets	
    total_current_assets = Column(Float)
    
    # Property, Plant & Equipment, Net	
    net_property_plant_equipment = Column(Float)
        # Property, Plant & Equipment	
    property_plant_equipment = Column(Float)
        # Accumulated Depreciation	
    accumulated_depreciation = Column(Float)
    
    # Long Term Investments & Receivables
    long_investments_receivables = Column(Float)
        # Long Term Investments	
    long_investments = Column(Float)
        # Long Term Marketable Securities
    long_marketable_securities = Column(Float)
        # Long Term Receivables	
    long_receivables = Column(Float)
    
    # Other Long Term Assets
    other_long_assets = Column(Float)   
        # Intangible Assets	
    intangible_assets = Column(Float)
        # Goodwill
    goodwill = Column(Float)	
        # Other Intangible Assets
    other_intangible_assets = Column(Float)	
        # Prepaid Expense
    prepaid_expenses = Column(Float)
        # Deferred Tax Assets (Long Term)
    long_deferred_tax_assets = Column(Float)
        # Derivative & Hedging Assets (Long Term)	
    long_derivative_hedging_assets = Column(Float)
        # Prepaid Pension Costs	
    prepaid_pension_costs = Column(Float)
        # Discontinued Operations (Long Term)
    long_discontinued_operation = Column(Float)
        # Investments in Affiliates	
    investment_affiliates = Column(Float)
        # Misc. Long Term Assets
    misc_long_assets = Column(Float)
    
    # Total Noncurrent Assets	
    total_noncurrent_assets = Column(Float)
    # Total Assets	
    total_assets = Column(Float)
    
    # Payables & Accruals
    payables_accruals = Column(Float)
        # Accounts Payable
    accounts_payable = Column(Float)
        # Accrued Taxes	
    accrued_taxes = Column(Float)
        # Interest & Dividends Payable	
    interest_dividends_payable = Column(Float)
        # Other Payables & Accruals	
    other_payables_accruals = Column(Float)
    
    # Short Term Debt	
    short_debt = Column(Float)
        # Short Term Borrowings	
    short_borrowings = Column(Float)
        # Short Term Capital Leases	
    short_capital_leases = Column(Float)
        # Current Portion of Long Term Debt	
    current_portion_of_long_debt = Column(Float)
    
    # Other Short Term Liabilities
    other_short_liabilities = Column(Float)	
        # Deferred Revenue (Short Term)	
    short_deferred_revenue = Column(Float)
        # Liabilities from Derivatives & Hedging (Short Term)	
    short_liabilities_from_derivatives_hedging = Column(Float)
        # Deferred Tax Liabilities (Short Term)	
    short_deferred_tax_liabilities = Column(Float) 
        # Liabilities from Discontinued Operations (Short Term)
    short_liabilities_from_discountinued_operations = Column(Float)
        # Misc. Short Term Liabilities	
    misc_short_liabilities = Column(Float)
    
    # Total Current Liabilities	
    total_current_liabilities = Column(Float)
    
    # Long Term Debt
    long_debt = Column(Float)	
        # Long Term Borrowings
    long_borrowings = Column(Float)
        # Long Term Capital Leases	
    long_capital_leases = Column(Float)
    
    # Other Long Term Liabilities	
    other_long_liabilities = Column(Float)
        # Accrued Liabilities	
    accrued_liabilities = Column(Float)
        # Pension Liabilities
    pension_liabilities = Column(Float)
            # Pensions	
    pensions = Column(Float)
            # Other Post-Retirement Benefits
    other_postretirement_benefits = Column(Float)
        # Deferred Compensation	
    deferred_compensation = Column(Float)
        # Deferred Revenue (Long Term)	
    long_deferred_revenue = Column(Float)
        # Deferred Tax Liabilities (Long Term)
    long_deferred_tax_liabilities = Column(Float)
        # Liabilities from Derivatives & Hedging (Long Term)
    long_liabilities_derivatives_hedging = Column(Float)
        # Liabilities from Discontinued Operations (Long Term)
    long_liabilities_discountinued_operations = Column(Float)
        # Misc. Long Term Liabilities	
    misc_long_liabilities = Column(Float)
    
    # Total Noncurrent Liabilities	
    total_noncurrent_liabilities = Column(Float)
    # Total Liabilities	
    total_liabilities = Column(Float)
    
    # Preferred Equity
    preferred_equity = Column(Float)
    # Share Capital & Additional Paid-In Capital
    chare_capial_additional_paidin_capital = Column(Float)	
        # Common Stock	
    common_stock = Column(Float)
        # Additional Paid in Capital
    additional_paidin_capital = Column(Float)
        # Other Share Capital	
    other_share_capital = Column(Float)

    # Treasury Stock	
    treasury_stock = Column(Float)
    # Retained Earnings	
    retained_earnings = Column(Float)
    # Other Equity
    other_equity = Column(Float)
	
    # Equity Before Minority Interest	
    equity_before_minority_interest = Column(Float)
    # Minority Interest	
    minority_interest = Column(Float)
    # Total Equity	
    total_equity = Column(Float)
    # Total Liabilities & Equity 
    total_liabilities_equity = Column(Float)

    # bank 
    #
	# Cash, Cash Equivalents & Short Term Investments	
    # Interbank Assets						
    fi_interbank_Assets	= Column(Float)
        # Fed Funds Sold & Repos
    fi_fed_funds_sold_Repos	= Column(Float)
        # Other Interbank Assets
    fi_other_interbank_assets = Column(Float)

    # Short & Long Term Investments
    fi_short_long_investments = Column(Float)
        # Trading Securities	
    fi_trading_securities = Column(Float)
        # Investment Securities Available for Sale	
    fi_investment_securities_available_for_sale = Column(Float)
        # Investment Securities Held to Maturity
    fi_investment_securities_held_to_maturity = Column(Float)
        # Real Estate Investments
    fi_real_estate_investments = Column(Float)
        # Other Investments	
    fi_other_investments = Column(Float)
    
    # Accounts & Notes Receivable
    
    # Net Loans	
    fi_net_loans = Column(Float)
        # Reserve for Loan Losses	
    fi_reserve_for_loan_losses = Column(Float)
        # Total Loans	
    fi_total_loans = Column(Float)
    
    
    # Total Commercial Loans
    fi_total_commercial_loans = Column(Float)	
        # Commercial Real Estate Loans	
    fi_commercial_real_estate_loans = Column(Float)
        # Other Commercial Loans
    fi_other_coummercial_loans = Column(Float)	
    
    # Total Consumer Loans	
    fi_total_consumer_loans = Column(Float)
        # Credit Card Loans	
    fi_credit_card_loans = Column(Float)
        # Home Equity Loans	
    fi_home_equity_loans = Column(Float)
        # Family Residential Loans
    fi_family_residential_loans = Column(Float)
        # Auto Loans	
    fi_auto_loans = Column(Float)
        # Student Loans	
    fi_student_loans = Column(Float)
        # Other Consumer Loans
    fi_other_consumer_loans = Column(Float)

    # Other Loans
    fi_other_loans = Column(Float)

    # Net Fixed Assets	
    fi_net_fixed_assets = Column(Float)
        # Property, Plant & Equipment, Net
        # Operating Lease Assets
    fi_operating_lease_assets = Column(Float)
        # Other Fixed Assets
    fi_other_fixed_assets = Column(Float)
    
    # Intangible Assets	
    # Goodwill
    # Other Intangible Assets
    # Investments in Associates	
    # Deferred Tax Assets (Short Term)	
    # Derivatives & Hedging (Assets)
    fi_derivatives_hedging_assets = Column(Float)	
    # Discontinued Operations (Assets)
    fi_discontinued_operations_assets = Column(Float)	
    # Customer Acceptances & Liabilities
    fi_customer_acceptances_liabilities = Column(Float)	
    
    # Other Assets	   	
    fi_other_assets = Column(Float)
    # Total Assets
    
    # Total Deposits
    fi_total_deposits = Column(Float)	
        # Demand Deposits	
    fi_demand_deposits = Column(Float)
        # Interest Bearing Deposits	
    fi_interest_bearing_deposits = Column(Float)
        # Saving Deposits	
    fi_saving_deposits = Column(Float)
        # Time Deposits	
    fi_time_deposits = Column(Float)
        # Other Deposits
    fi_other_deposits = Column(Float)
    

    # Short Term Debt
        # Securities Sold Under Repo
    fi_securities_sold_under_repo = Column(Float)
        # Trading Account Liabilities
    fi_trading_account_liabilities = Column(Float)
        # Short Term Capital Leases	
        # Current Portion of Long Term Debt	
        # Short Term Borrowings	
        # Payables Broker Dealers	
    fi_payables_broker_dealers = Column(Float)
    
   
    # Long Term Debt
        # Long Term Capital Leases
        # Long Term Borrowings	
    
    # Pension Liabilities	
        # Pensions	
        # Other Post-Retirement Benefits

    # Deferred Tax Liabilities (Short Term)
    # Derivatives & Hedging (Liabilities)	
    fi_derivatives_hedging_liabilities = Column(Float)
    # Discontinued Operations (Liabilities)
    fi_discontinued_operations_liabilities = Column(Float)
    # Other Liabilities
    # Total Liabilities	

    # Insurance 
    # Total Investments	
    fi_total_investments = Column(Float)
        # Fixed Income-Trading/AFS & Short Term Inv.
    fi_fixed_income_trading_AFS_short_investment = Column(Float)
        # Loans & Mortgages	
    fi_loans_mortgages = Column(Float)
        # Fixed Income Securities HTM	
    fi_fixed_income_securities_HTM = Column(Float)
        # Equity Securities	
    fi_equity_securities = Column(Float)
        # Real Estate Investments	
    fi_real_estate_investments = Column(Float)
        # Other Investments
    fi_other_investments = Column(Float)
    # Cash, Cash Equivalents & Short Term Investments
    # Accounts & Notes Receivable
    # Property, Plant & Equipment, Net
    # Deferred Policy Acquisition Costs
    fi_deferred_policy_aquisition_costs = Column(Float)
    # Other Assets
    # Total Assets

    # Insurance Reserves 
    fi_insurance_reserves = Column(Float)
        # Reserve for Outstanding Claims & Losses
    fi_reserve_outstanding_claims_losses = Column(Float)
        # Premium Reserve (Unearned)
    fi_unearned_premium_reserve = Column(Float)
        # Life Policy Benefits	
    fi_life_policy_benefits = Column(Float)
        # Other Insurance Reserves
    fi_other_insurance_reserves = Column(Float)
    
    # Short Term Debt
    # Other Short Term Liabilities
    # Long Term Debt
    # Pension Liabilities
        # Pensions
        # Other Post-Retirement Benefits
    # Other Long Term Liabilities	
    # Funds for Future Appropriations	
    fi_funds_future_appropriation = Column(Float)
    # Total Liabilities

    
class IncomeStatement(FinanceBase, Mixin):

    @classmethod
    def important_cols(cls):
        return ['operating_income', 'investment_income', 'total_operating_costs', 'total_profits', 'sales_costs',
                'managing_costs', 'financing_costs']

    __tablename__ = 'income_statement'

    provider = Column(String(length=32))
    code = Column(String(length=32))

    report_period = Column(String(length=32))
    report_date = Column(DateTime)
    restated_date = Column(DateTime)

    basic_shares = Column(Float)
    diluted_shares = Column(Float)

    # Revenue
    revenue = Column(Float) 
        # Sales & Services Revenue
    sales_servies_revenue = Column(Float)
        # Financing Revenue
    financing_revenue = Column(Float)
        # Other Revenue
    other_revenue = Column(Float)
    
    # Cost of Revenue
    cost_revenue = Column(Float)
        # Cost of Goods & Services
    cost_goods_services = Column(Float)
        # Cost of Financing Revenue
    cost_financing_revenue = Column(Float)
        # Cost of Other Revenue
    cost_other_revenue = Column(Float)
    # Gross Profit (revenue + cost of revenue)
    gross_profit = Column(Float)
    # Other Operating Income
    other_operating_income = Column(Float)
    # Operating Expenses
    operating_expenses = Column(Float)
        # Selling, General & Administrative
    selling_general_administrative = Column(Float)
        # Selling & Marketing
    selling_marketing = Column(Float)
        # General & Administrative
    general_administrative = Column(Float)
        # Research & Development
    research_development = Column(Float)
        # Depreciation & Amortization
    depreciation_amortization = Column(Float)
        # Provision for Doubtful Accounts
    provision_doubtful_accounts = Column(Float)
        # Other Operating Expenses
    other_operating_expenses = Column(Float)
    # Operating Income (Loss) (gross profit + other operating income + operating expenses)
    operating_income = Column(Float)
    # Non-Operating Income (Loss)
    nonoperating_income = Column(Float)
        # Interest Expense, Net(interest_expense + interest_income)
    net_interest_expense = Column(Float)
            # Interest Expense
    interest_expense = Column(Float)
            # Interest Income
    interest_income = Column(Float)
        # Other Investment Income (Loss)
    other_investment_income = Column(Float)
            # Foreign Exchange Gain (Loss)
    foreign_exchange_gain = Column(Float)
            # Income (Loss) from Affiliates
    income_from_affliates = Column(Float)
        # Other Non-Operating Income (Loss)
    other_nonoperating_income = Column(Float)
    # Pretax Income (Loss), Adj. (operating income + nonoperating income)
    adj_pretax_income = Column(Float)
    # Abnormal Gains (Losses)
    abnormal_gains = Column(Float)
        # Acquired In-Process R&D
    acquired_inprocess_R_D = Column(Float)
        # Merger & Acquisition Expense
    merger_acquisition_expense = Column(Float)
        # Abnormal Derivatives
    abnormal_derivatives = Column(Float)
        # Disposal of Assets
    disposal_assets = Column(Float)
        # Early Extinguishment of Debt
    early_extinguishment_debt = Column(Float)
        # Asset Write-Down
    asset_writedown = Column(Float)
        # Impairment of Goodwill & Intangibles
    impairment_goodwill_intangibles = Column(Float)
        # Sale of Business
    sale_business = Column(Float)
        # Legal Settlement
    legal_settlement = Column(Float)
        # Restructuring Charges
    restructuring_charges = Column(Float)
        # Sale of Investments & Unrealized Investments
    sales_investments_unrealized_investments = Column(Float)
        # Insurance Settlement
    insurance_settlement = Column(Float)
        # Other Abnormal Items
    other_abnormal_items = Column(Float)
    # Pretax Income (Loss) (adj pretax income + abnormal income)
    pretax_income = Column(Float)
    # Income Tax (Expense) Benefit, Net 
    net_income_tax_benefit = Column(Float)
        # Current Income Tax
    current_income_tax = Column(Float)
        # Deferred Income Tax
    deferred_income_tax = Column(Float)
        # Tax Allowance/Credit
    tax_allowance_credit = Column(Float)
        # Income (Loss) from Affiliates, Net of Taxes
    income_affliates_net_taxes = Column(Float)
    # Income (Loss) from Continuing Operations (pretax income + income tax benefit, net)
    income_continuing_operations = Column(Float)
    # Net Extraordinary Gains (Losses)
    net_extraordinary_gains = Column(Float)
        # Discontinued Operations
    discontinued_operations = Column(Float)
        # Accounting Charges & Other
    accounting_charges_other = Column(Float)
    # Income (Loss) Incl. Minority Interest (income from continuing operation + net extraordinary gain)
    income_incl_minority_interest = Column(Float)
    # Minority Interest
    minority_interest = Column(Float)
    # Net Income
    net_income = Column(Float)
    # Preferred Dividends 
    preferred_dividends = Column(Float)
    # Other Adjustments
    other_adjustments = Column(Float)
    # Net Income (Common)
    net_common_income = Column(Float)

    # Bank
    # Revenue
        # Net Interest Income 
    fi_net_interest_income = Column(Float)
            # Total Interest Income
    fi_total_interest_income = Column(Float)
            # Total Interest Expense
    fi_total_interest_expense = Column(Float)
        # Total Non-Interest Income
    fi_total_noninterest_income = Column(Float)
            # Trading Account Profits/Losses
    fi_trading_account_profits_losses = Column(Float)
            # Investment Income (Loss)
    fi_investment_income = Column(Float)
            # Sale of Loan Income (Loss)
    fi_sale_loan_income = Column(Float)
            # Commissions & Fees Earned
    fi_commissions_fee_earned = Column(Float)
            # Net OTTI Losses Recognised in Earnings
    fi_net_otti_losses_recognised_earnings = Column(Float)
            # Other Non-Interest Income
    fi_other_noninterest_income = Column(Float)
    # Provision for Loan Losses
    fi_provision_loan_losses = Column(Float)

    # Net Revenue after Provisions (revenue - provision for loan losses)
    fi_net_revenue_after_provisions = Column(Float)
    # Total Non-Interest Expense
    fi_total_noninterest_expense = Column(Float)
        # Commissions & Fees Paid
    fi_commissions_fee_paid = Column(Float)
        # Other Operating Expenses
    # Operating Income
    # Non-Operating Income (Loss)
        # Income (Loss) from Affiliates
        # Other Non-Operating Income (Loss)
    # Pretax Income (Loss), Adj. (operation income + non-operating income)
    # Abnormal Gains (Losses)
        # Debt Valuation Adjustment
    fi_debt_valuation_adjustment = Column(Float)
        # Credit Valuation Adjustment
    fi_credit_valuation_adjustment = Column(Float)
        # Merger & Acquisition Expense
        # Disposal of Assets
        # Early Extinguishment of Debt
        # Asset Write-Down
        # Impairment of Goodwill & Intangibles
        # Sale of Business
        # Legal Settlement
        # Restructuring Charges
        # Other Abnormal Items
    # Pretax Income (Loss) (pre income + abnormal gains)
    # Income Tax (Expense) Benefit, Net
        # Current Income Tax	
        # Deferred Income Tax	
        # Tax Allowance/Credit	
        # Income (Loss) from Affiliates, Net of Taxes

    # Income (Loss) from Continuing Operations (pretax income + income tax benefit)
    # Net Extraordinary Gains (Losses)
        # Discontinued Operations
        # Accounting Charges & Other

    # Income (Loss) Incl. Minority Interest
    # Minority Interest
    # Net Income
    # Preferred Dividends
    # Other Adjustments
    # Net Income (Common)

    # (insurance)
    # Revenue 
        # Net Premiums Earned
    fi_net_preminums_earned = Column(Float)
        # Investment Income (Loss)
        # Income from Real Estate
    fi_income_real_estate = Column(Float)
        # Other Operating Income
            # Policy Charges & Fees
    fi_policy_charges_fees = Column(Float)
            # Total Realized Investment Gains
    fi_total_realized_investment_gains = Column(Float)
            # Total OTTI Realized
    fi_total_otti_realized = Column(Float)
            # Other Realized Investment Gains
    fi_other_realized_investment_gains = Column(Float)
            # Other Income
    fi_other_income = Column(Float)

    # Total Claims & Losses
    fi_total_claims_losses = Column(Float)
        # Claims & Losses
    fi_claims_losses = Column(Float)
        # Long Term Charges
    fi_long_charges = Column(Float)
        # Other Claims & Losses
    fi_other_claims_losses = Column(Float)
    # Underwriting Expense & Acquisition Cost
    fi_underwriting_expense_aquisition_cost = Column(Float)
    # Other Operating Expenses
    # Operating Income (Loss) (revenue + total claim + underwriting expense + other operating expenses)
    # Non-Operating Income (Loss)
        # Income (Loss) from Affiliates 
        # Interest Expense, Net
        # Other Non-Operating Income (Loss)

    # Pretax Income (Loss), Adj.
    # Abnormal Gains (Losses)
        # Merger & Acquisition Expense	
        # Abnormal Derivatives	
        # Disposal of Assets	
        # Early Extinguishment of Debt	
        # Asset Write-Down	
        # Impairment of Goodwill & Intangibles	
        # Sale of Business	
        # Legal Settlement	
        # Restructuring Charges	
        # Net Investment Losses	
    fi_net_investment_losses = Column(Float)
        # Foreign Exchange	
    fi_foreign_exchange = Column(Float)
        # Other Abnormal Items
    
class CashFlowStatement(FinanceBase, Mixin):

    @classmethod
    def important_cols(cls):
        return ['operating_income', 'investment_income', 'total_operating_costs', 'total_profits', 'sales_costs',
                'managing_costs', 'financing_costs']

    __tablename__ = 'cashflow_statement'

    provider = Column(String(length=32))
    code = Column(String(length=32))

    report_period = Column(String(length=32))
    report_date = Column(DateTime)
    restated_date = Column(DateTime)

    basic_shares = Column(Float)
    diluted_shares = Column(Float)


    # Operating Activities
    # Net Income/Starting Line
    net_income_starting_line = Column(Float)
        # Net Income
    net_income = Column(Float)
        # Net Income from Discontinued Operations
    net_income_discontinued_operations = Column(Float)
        # Other Adjustments
    other_adjustments = Column(Float)
    # Depreciation & Amortization
    depreciation_amortization = Column(Float)
    # Non-Cash Items
    noncash_items = Column(Float)
        # Stock-Based Compensation
    stockbased_compensation = Column(Float)
        # Deferred Income Taxes
    deferred_income_taxes = Column(Float)
        # Other Non-Cash Adjustments
    other_noncash_adjustments = Column(Float)
    # Change in Working Capital
    change_working_capital = Column(Float)
            # Change in Accounts Receivable
    change_accounts_receivable = Column(Float)
            # Change in Inventories
    change_inventories = Column(Float)
            # Change in Accounts Payable
    change_accounts_payable = Column(Float)
            # Change in Other
    change_other = Column(Float)

    operating_net_cash_discontinued_operation = Column(Float)
    net_cash_operation_activities = Column(Float)

    # Investment Activities
    # Change in Fixed Assets & Intangibles
    change_fiexed_assets_intangibles = Column(Float)
        # Disposition of Fixed Assets & Intangibles
    disposition_fixed_assets_intangibles = Column(Float)
            # Disposition of Fixed Assets
    disposition_fixed_assets = Column(Float)
            # Disposition of Intangible Assets
    disposition_intangible_assets = Column(Float)
        # Acquisition of Fixed Assets & Intangibles
    acquisition_fixed_assets_intangibles = Column(Float)
            # Purchase of Fixed Assets
    purchase_fixed_assets = Column(Float)
            # Acquisition of Intangible Assets
    aquisition_intangible_assets = Column(Float)
            # Other Change in Fixed Assets & Intangibles
    other_change_fixed_assets_intangibles = Column(Float)
    # Net Change in Long Term Investment
    net_change_long_investment = Column(Float)
        # Decrease in Long Term Investment
    decrease_long_investment = Column(Float)
        # Increase in Long Term Investment
    increase_long_investment = Column(Float)
    # Net Cash from Acquisitions & Divestitures
    net_cash_acquisitions_divestitures = Column(Float)
        # Net Cash from Divestitures
    net_cash_divestitures = Column(Float)
        # Cash for Acquisition of Subsidiaries
    cash_acquisition_subsidiaries = Column(Float)
        # Cash for Joint Ventures
    cash_joint_ventures = Column(Float)
        # Net Cash from Other Acquisitions
    net_cash_other_aquisitions = Column(Float)
    # Other Investing Activities
    other_investing_activities = Column(Float)
    # Net Cash from Discontinued Operations (Investing)
    investing_net_cash_discontinued_operation = Column(Float)
    # Net Cash from Investing Activities
    net_cash_investing_activites = Column(Float)

    # Financing Activities 
    #
    dividends_paid = Column(Float)
    # Cash from (Repayment of) Debt
    cash_repayment_debt = Column(Float)
        # Cash from (Repayment of) Short Term Debt, Net
    net_cash_repayment_short_debt = Column(Float)
        # Cash from (Repayment of) Long Term Debt, Net
    net_cash_repayment_long_debt = Column(Float)
            # Cash from Long Term Debt
    repayments_long_debt = Column(Float)
            # Cash from Long Term Debt
    cash_long_debt = Column(Float)
    # Cash from (Repurchase of) Equity
    cash_repurchase_equity = Column(Float)
        # Increase in Capital Stock
    increase_capital_stock = Column(Float)
        # Decrease in Capital Stock
    decrease_capital_stock = Column(Float)
    # Other Financing Activities
    other_financing_activities = Column(Float)
    # Net Cash from Discontinued Operations (Financing)
    financing_net_cash_discontinued_operation = Column(Float)
    # Net Cash from Financing Activities
    net_cash_financing_activities = Column(Float)

    # Total 
    # Net Cash Before Disc. Operations and FX
    net_cash_before_disc_operations_fx = Column(Float)
        # Change in Cash from Disc. Operations and Other
    change_cash_disc_operations_other = Column(Float)
    # Net Cash Before FX(the sum of the above two items)
    net_cash_before_fx = Column(Float)
    # Effect of Foreign Exchange Rates
    effect_foreign_exchange_rates = Column(Float)
    # Net Change in Cash
    net_change_cash = Column(Float)

    # Bank
    # Net Income/Starting Line	
        # Net Income	
        # Net Income from Discontinued Operations	
        # Other Adjustments	
    
    # Depreciation & Amortization	
    # Provision for Loan Losses	
    fi_provision_loan_losses = Column(Float)
        # Non-Cash Items	
            # Gain On Sale of Securities & Loans
    fi_gain_sales_securities_loans = Column(Float)
            # Deferred Income Taxes
            # Stock-Based Compensation
            # Other Non-Cash Adjustments
        # Change in Working Capital
            # Trading Assets & Liabilities
    fi_trading_assets_liabilities = Column(Float)
            # Net Change of Investments
    fi_net_change_of_investments = Column(Float)
            # Net Change of Interbank Assets
    fi_net_change_interbank_assets = Column(Float)
            # Net Change of Interbank Liabilities 
    fi_net_change_interbank_liabilities = Column(Float)
            # Net Change in Operating Loans
    fi_net_change_operating_loans = Column(Float)
            # Accrued Interest Receivable
    fi_accrued_interest_receivable = Column(Float)
            # Accrued Interest Payable
    fi_accrued_interest_payable = Column(Float)
            # Other Operating Assets/Liabilities
    fi_other_operating_assets_liabilities = Column(Float)
        # Net Cash from Discontinued Operations (Operating)
    
        # Net Cash from Operating Activities

    # Investing Activities
    # Change in Fixed Assets & Intangibles
        # Disposition of Fixed Assets & Intangibles
        # Capital Expenditures
    fi_capital_expenditure = Column(Float)
    # Net Change in Investments
    fi_net_change_in_investments = Column(Float)
        # Decrease in Investments
    fi_decrease_investments = Column(Float)
            # Decrease in HTM Investments
    fi_decrease_htm_investments = Column(Float)
            # Decrease in AFS Investments
    fi_decrease_afs_investments = Column(Float)
        # Increase in Investments
    fi_increase_investments = Column(Float)
            # Increase in HTM Investments
    fi_increase_htm_investments = Column(Float)
            # Increase in AFS Investments
    fi_increase_afs_investments = Column(Float)
        # Net Change in Other Investments
    fi_net_change_other_investments = Column(Float)
        # Net Change in Loans & Interbank
    fi_net_change_loans_interbank = Column(Float)
            # Net Change in Customer Loans
    fi_net_change_customer_loans = Column(Float)
            # Net Change in Interbank Assets
    fi_net_change_interbank_assets = Column(Float)
            # Net Change in Other Loans
    fi_net_change_other_loans = Column(Float)
        
        # Net Cash from Acquisitions & Divestitures
            # Net Cash from Divestitures
            # Cash for Acquisition of Subsidiaries
            # Cash for Joint Ventures
            # Net Cash from Other Acquisitions

        # Other Investing Activities
        # Net Cash from Discontinued Operations (Investing)
        # Net Cash from Investing Activities

        # Financing Activities 
        # Dividends Paid
        # Cash from (Repayment of) Debt
            # Cash from (Repayment of) Short Term Debt, Net
            # Net Change in Interbank Transfers
    fi_net_change_interbank_transfers = Column(Float)
            # Cash from (Repayment of) Long Term Debt, Net
                # Repayments of Long Term Debt
                # Cash from Long Term Debt
        # Cash from (Repurchase of) Equity
            # Increase in Capital Stock
            # Decrease in Capital Stock
        # Net Change In Deposits
    fi_net_change_deposits = Column(Float)
        # Other Financing Activities
        # Net Cash from Discontinued Operations (Financing)
        # Net Cash from Financing Activities

        # Net Cash Before Disc. Operations and FX (net cash from all three activities)
        # Change in Cash from Disc. Operations and Other
        # Net Cash Before FX
        # Effect of Foreign Exchange Rates
        # Net Change in Cash
    
    # Insurance 

    # Fanancing Activities 
    # Dividends Paid
    # Cash from (Repayment of) Debt
        # Cash from (Repayment of) Long Term Debt, Net
            # Repayments of Long Term Debt
            # Cash from Long Term Debt
    # Cash from (Repurchase of) Equity
        # Increase in Capital Stock
        # Decrease in Capital Stock
    # Change in Insurance Reserves
    fi_change_insurance_recerves = Column(Float)
    # Other Financing Activities
    # Net Cash from Discontinued Operations (Financing)
    # Net Cash from Financing Activities


class FinanceFactor(FinanceBase, Mixin):
    @classmethod
    def important_cols(cls):
        return ['basic_eps', 'total_op_income', 'net_profit', 'op_income_growth_yoy', 'net_profit_growth_yoy', 'roe',
                'rota', 'gross_profit_margin', 'net_margin']

    __tablename__ = 'finance_factor'

    provider = Column(String(length=32))
    code = Column(String(length=32))

    report_period = Column(String(length=32))
    report_date = Column(DateTime)
    restated_date = Column(DateTime)
    # 每股指标
    #
    ebitda = Column(Float)
    total_debt = Column(Float)
    fcf = Column(Float)
    gross_profit_margin = Column(Float)
    operating_margin = Column(Float)
    net_profit_margin = Column(Float)
    roe = Column(Float)
    roa = Column(Float)
    fcf_net_income = Column(Float)
    current_ratio = Column(Float)
    liabilities_to_equity_ratio = Column(Float)
    debt_ratio = Column(Float)
    basic_eps = Column(Float)
    diluted_eps = Column(Float)
    sps = Column(Float)
    equity_ps = Column(Float)
    fcf_ps = Column(Float)
    dps = Column(Float)
    # Pietroski F-Score
    pietroski = Column(Float)

register_schema(providers=['simfin'], db_name='finance', schema_base=FinanceBase)

# the __all__ is generated
__all__ = ['BalanceSheet', 'IncomeStatement', 'CashFlowStatement', 'FinanceFactor']