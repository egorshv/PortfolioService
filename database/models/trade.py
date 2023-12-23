from enum import Enum

from sqlalchemy import Integer, Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from database.DBCore import Base
from schemas.currency import Currency
from schemas.trade import TradeMark


class Trade(Base):
    __tablename__ = 'trade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(4), nullable=False)
    action = Column(Enum(TradeMark))
    value = Column(Float, nullable=False)
    currency = Column(Enum(Currency), nullable=False)
    created_at = Column(DateTime, nullable=False)
    result = Column(Float, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)
    portfolio = relationship("Portfolio", backref=backref("trade_portfolio_id"), lazy='selectin',
                             foreign_keys=portfolio_id)

    def __init__(self, ticker, value, currency, created_at, result, portfolio_id):
        self.ticker = ticker
        self.value = value
        self.currency = currency
        self.created_at = created_at
        self.result = result
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f'{self.ticker} : {self.value} : {self.currency} : {self.created_at} : {self.result} : {self.potfolio_id}'
