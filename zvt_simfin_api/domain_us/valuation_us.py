# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import Mixin
from zvt.contract.register import register_schema

ValuationBase = declarative_base()


class StockValuation(ValuationBase, Mixin):
    __tablename__ = 'stock_valuation'

    code = Column(String(length=32))
    name = Column(String(length=32))
    
    # 市值
    market_cap = Column(Float)

    # 静态pe
    pe_q = Column(Float)
    # 动态pe
    pe_ttm = Column(Float)
    # 市净率
    pb = Column(Float)
    # 市销率
    ps_q = Column(Float)
    ps_ttm = Column(Float)
    # 市现率
    pcf_q = Column(Float)
    pcf_ttm = Column(Float)
    # 企业价值
    ev = Column(Float)
    ev_ebitda = Column(Float)
    ev_sales = Column(Float)
    ev_fcf = Column(Float)
    book_market = Column(Float)
    operating_income_ev = Column(Float)


class EtfValuation(ValuationBase, Mixin):
    __tablename__ = 'etf_valuation'

    code = Column(String(length=32))
    name = Column(String(length=32))
    # 静态pe
    pe = Column(Float)
    # 加权
    pe1 = Column(Float)
    # 动态pe
    pe_ttm = Column(Float)
    # 加权
    pe_ttm1 = Column(Float)
    # 市净率
    pb = Column(Float)
    # 加权
    pb1 = Column(Float)
    # 市销率
    ps = Column(Float)
    # 加权
    ps1 = Column(Float)
    # 市现率
    pcf = Column(Float)
    # 加权
    pcf1 = Column(Float)


register_schema(providers=['simfin'], db_name='valuation', schema_base=ValuationBase)

# the __all__ is generated
__all__ = ['StockValuation', 'EtfValuation']