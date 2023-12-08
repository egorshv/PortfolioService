from datetime import datetime

from pydantic import BaseModel


class State(BaseModel):
    USD_result: float
    RUB_result: float
    created_at: datetime
