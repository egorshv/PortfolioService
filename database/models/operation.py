from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from database.DBCore import Base


class Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)
    portfolio = relationship("Portfolio", backref=backref('operation_portfolio_id'), lazy='selectin',
                             foreign_keys=portfolio_id)

    def __init__(self, value, created_at, portfolio_id):
        self.value = value
        self.created_at = created_at
        self.portfolio_id = portfolio_id

    def __repr__(self):
        return f'{self.value} : {self.created_at} : {self.portfolio_id}'
