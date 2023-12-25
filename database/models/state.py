from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class State(Base):
    __tablename__ = 'state'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    usd_result: Mapped[float] = mapped_column(nullable=False)
    rub_result: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id", ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f'{self.created_at} : {self.portfolio_id}'
