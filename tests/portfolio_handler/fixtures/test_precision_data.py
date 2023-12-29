from datetime import datetime
from typing import List

import pytest

from schemas.currency import Currency
from schemas.trade import TradeMark, TradeSchema, TradeActionType


@pytest.fixture
def test_precision_marks() -> List[TradeMark]:
    return [TradeMark.TP] * 10 + [TradeMark.FP] * 40


@pytest.fixture
def test_precision_list(test_precision_marks) -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=1,
            ticker='VKCO',
            action=TradeActionType.BUY,
            value=700,
            currency=Currency.USD,
            created_at=datetime.now(),
            mark=mark
        )
        for i, mark in enumerate(test_precision_marks)
    ]


@pytest.fixture
def test_precision_answer() -> float:
    return 0.2


@pytest.fixture
def test_precision_zero_division() -> List[TradeSchema]:
    return []
