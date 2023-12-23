from sqlalchemy import Integer, Column, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from database.DBCore import Base


class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usd_result = Column(Float, nullable=False)
    rub_result = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)
    portfolio = relationship("Portfolio", backref=backref('state_portfolio_id'), lazy='selectin',
                             foreign_keys=portfolio_id)

    def __init__(self, usd_result, rub_result, created_at, portfolio_id):
        self.usd_result = usd_result
        self.rub_result = rub_result
        self.created_at = created_at
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f'{self.created_at} : {self.portfolio_id}'
