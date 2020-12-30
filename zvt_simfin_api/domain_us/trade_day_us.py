# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import Mixin
from zvt.contract.register import register_schema

TradeDayBase = declarative_base()


class USStockTradeDay(TradeDayBase, Mixin):
    __tablename__ = 'stock_trade_day'


register_schema(providers=['iex'], db_name='us_trade_day', schema_base=TradeDayBase)

__all__ = ['USStockTradeDay']