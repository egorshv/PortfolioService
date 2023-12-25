from typing import Optional

from pydantic import BaseModel


class PortfolioSchema(BaseModel):
    name: str
    last_precision: Optional[float] = 0
    last_recall: Optional[float] = 0
    user_id: int
    deposited_money: int = 0
