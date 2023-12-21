from datetime import datetime

from pydantic import BaseModel


class Operation(BaseModel):
    value: float
    created_at: datetime
