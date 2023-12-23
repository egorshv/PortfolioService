from datetime import datetime

from pydantic import BaseModel


class State(BaseModel):
    id: int
    portfolio_id: int
    USD_result: float
    RUB_result: float
    created_at: datetime
