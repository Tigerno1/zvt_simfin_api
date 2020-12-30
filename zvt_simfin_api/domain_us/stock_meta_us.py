# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, DateTime, BigInteger, Float
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract import EntityMixin
from zvt.contract.register import register_schema, register_entity
from zvt.utils.time_utils import now_pd_timestamp

StockMetaBase = declarative_base()


class BaseSecurity(EntityMixin):
    # 上市日
    list_date = Column(DateTime)
    # 退市日
    end_date = Column(DateTime)

class BasePortfolio(BaseSecurity):
    @classmethod
    def get_stocks(cls,
                   code=None, codes=None, ids=None, timestamp=now_pd_timestamp(), provider=None):
        """

        :param code: portfolio(etf/block/index...) code
        :param codes: portfolio(etf/block/index...) codes
        :param timestamp:
        :param provider:
        :return:
        """
        portfolio_stock: BasePortfolioStock = eval(f'{cls.__name__}Stock')
        return portfolio_stock.query_data(provider=provider, code=code, codes=codes, ids=ids)

@register_entity(entity_type='stock')
class Stock(StockMetaBase, BaseSecurity):
    __tablename__ = 'stock'


@register_entity(entity_type='stock_industry')
class StockIndustry(StockMetaBase, BaseSecurity):
    __tablename__ = 'stock_industry'
    sectors = Column(String)
    industries = Column(String)


@register_entity(entity_type='etf')
class Etf(StockMetaBase, BasePortfolio):
    __tablename__ = 'etf'
    category = Column(String(length=64))

    @classmethod
    def get_stocks(cls, code=None, codes=None, ids=None, timestamp=now_pd_timestamp(), provider=None):
        from zvt.api.quote import get_etf_stocks
        return get_etf_stocks(code=code, codes=codes, ids=ids, timestamp=timestamp, provider=provider)


@register_entity(entity_type='stock_detail')
class StockDetail(StockMetaBase, BaseSecurity):
    __tablename__ = 'stock_detail'

    industries = Column(String)
    industry_indices = Column(String)
    concept_indices = Column(String)
    area_indices = Column(String)

    # 成立日期
    date_of_establishment = Column(DateTime)
    # 公司简介
    profile = Column(String(length=1024))
    # 主营业务
    main_business = Column(String(length=512))
    # 发行量(股)
    issues = Column(BigInteger)
    # 发行价格
    price = Column(Float)
    # 募资净额(元)
    raising_fund = Column(Float)
    # 发行市盈率
    issue_pe = Column(Float)
    # 网上中签率
    net_winning_rate = Column(Float)



register_schema(providers=['alphavantage', 'simfin'], db_name='stock_meta',
                schema_base=StockMetaBase)

# the __all__ is generated
__all__ = ['StockIndustry', 'StockDetail', 'Stock', 'Etf']