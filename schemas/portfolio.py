from typing import Optional

from pydantic import BaseModel


class Portfolio(BaseModel):
    id: int
    name: str
    precision: Optional[float] = 0
    recall: Optional[float] = 0
    user_id: int
    deposited_money: int = 0
