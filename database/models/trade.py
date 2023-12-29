from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base
from schemas.currency import Currency
from schemas.trade import TradeActionType, TradeMark


class Trade(Base):
    __tablename__ = 'trade'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    ticker: Mapped[str] = mapped_column(nullable=False)
    action: Mapped[TradeActionType] = mapped_column(nullable=False)
    mark: Mapped[TradeMark] = mapped_column(nullable=True, default=None)
    value: Mapped[float] = mapped_column(nullable=False)
    currency: Mapped[Currency] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    result: Mapped[float] = mapped_column(nullable=True, default=None)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id", ondelete='CASCADE'), nullable=False,
                                              index=True)
    portfolio = relationship(
        "Portfolio",
        back_populates="trades"
    )

    def __repr__(self):
        return f'{self.ticker} : {self.value} : {self.currency} : {self.created_at} : {self.result} : {self.potfolio_id}'
