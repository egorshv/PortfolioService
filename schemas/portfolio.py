import uuid
from typing import List, Optional

from pydantic import BaseModel

from schemas.state import State
from schemas.trade import Trade


class Portfolio(BaseModel):
    name: str
    precision: Optional[float] = None
    recall: Optional[float] = None
    user_id: int
    trades: List[Trade] = []
    states: List[State] = []
