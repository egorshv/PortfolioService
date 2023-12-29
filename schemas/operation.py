from datetime import datetime

from pydantic import BaseModel


class OperationSchema(BaseModel):
    id: int
    portfolio_id: int
    value: float
    created_at: datetime
