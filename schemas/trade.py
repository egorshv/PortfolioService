import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TradeActionType(str, Enum):
    BUY = 'buy'
    SELL = 'sell'


class TradeCurrency(str, Enum):
    RUB = 'rub'
    USD = 'usd'
    CNY = 'cny'


class TradeMark(str, Enum):
    TP = 'tp'
    TN = 'tn'
    FP = 'fp'
    FN = 'fn'


class Trade(BaseModel):
    ticker: str
    action: TradeActionType
    value: float
    currency: TradeCurrency
    created_at: datetime
    result: Optional[float] = None
    mark: Optional[TradeMark] = None
