from datetime import datetime

from pydantic import BaseModel


class Operation(BaseModel):
    id: int
    portfolio_id: int
    value: float
    created_at: datetime
    portfolio_name: str
