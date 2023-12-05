import uuid
from datetime import datetime

from pydantic import BaseModel


class State(BaseModel):
    id: uuid.UUID
    USD_result: float
    RUB_result: float
    created_at: datetime
