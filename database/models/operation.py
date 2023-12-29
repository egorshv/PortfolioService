from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.models.base import Base


class Operation(Base):
    __tablename__ = 'operation'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    value: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id", ondelete="CASCADE"), nullable=False,
                                              index=True)
    portfolio = relationship(
        "Portfolio",
        back_populates="operations"
    )

    def __repr__(self):
        return f'{self.value} : {self.created_at} : {self.portfolio_id}'
