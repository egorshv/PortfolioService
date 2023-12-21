from typing import List, Optional

from pydantic import BaseModel

from schemas.operation import Operation
from schemas.state import State
from schemas.trade import Trade


class Portfolio(BaseModel):
    name: str
    precision: Optional[float] = 0
    recall: Optional[float] = 0
    user_id: int
    trades: List[Trade] = []
    states: List[State] = []
    deposited_money: int = 0
    operations: List[Operation] = []
