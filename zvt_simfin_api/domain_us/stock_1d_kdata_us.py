# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain_us.stock_price_common_us import USStockKdataCommon

KdataBase = declarative_base()


class USStock1dKdata(KdataBase, USStockKdataCommon):
    __tablename__ = 'stock_1d_kdata'


register_schema(providers=['alphavantage', 'simfin'], db_name='us_stock_1d_kdata', schema_base=KdataBase)

# the __all__ is generated
__all__ = ['USStock1dKdata']