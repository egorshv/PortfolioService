from typing import List

from sqlalchemy.orm import relationship, Mapped, mapped_column

from database.models.base import Base
from database.models.operation import Operation
from database.models.state import State
from database.models.trade import Trade


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_precision: Mapped[float] = mapped_column(default=0)
    last_recall: Mapped[float] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(nullable=False)
    deposited_money: Mapped[float] = mapped_column(default=0)
    trades: Mapped[List[Trade]] = relationship()
    states: Mapped[List[State]] = relationship()
    operations: Mapped[List[Operation]] = relationship()

    def __repr__(self):
        return f'ID: {self.user_id} Name: {self.name}'
