import uuid
from typing import List

from pydantic import BaseModel

from schemas.state import State
from schemas.trade import Trade


class Portfolio(BaseModel):
    id: uuid.UUID
    name: str
    precision: float
    recall: float
    user_id: int
    trades: List[Trade]
    states: List[State]
