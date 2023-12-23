from datetime import datetime
from enum import Enum
from typing import Optional
from schemas.currency import Currency

from pydantic import BaseModel


class TradeActionType(str, Enum):
    BUY = 'buy'
    SELL = 'sell'


class TradeMark(str, Enum):
    TP = 'tp'
    TN = 'tn'
    FP = 'fp'
    FN = 'fn'


class Trade(BaseModel):
    id: int
    portfolio_id: int
    ticker: str
    action: TradeActionType
    value: float
    currency: Currency
    created_at: datetime
    result: Optional[float] = None
    mark: Optional[TradeMark] = None
