from datetime import datetime

from pydantic import BaseModel


class StateSchema(BaseModel):
    id: int
    portfolio_id: int
    usd_result: float
    rub_result: float
    created_at: datetime
