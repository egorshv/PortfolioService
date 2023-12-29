from datetime import datetime
from typing import List

import pytest

from schemas.currency import Currency
from schemas.trade import TradeMark, TradeSchema, TradeActionType


@pytest.fixture
def test_marks1() -> List[TradeMark]:
    return [TradeMark.FN] * 3 + [TradeMark.TP]


@pytest.fixture
def test_trade_set1(test_marks1) -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=1,
            ticker='SBER',
            action=TradeActionType.BUY,
            value=300,
            currency=Currency.RUB,
            created_at=datetime.now(),
            mark=mark
        )
        for i, mark in enumerate(test_marks1)
    ]


@pytest.fixture
def test_trade_set2() -> List[TradeSchema]:
    return []


@pytest.fixture
def test_recall_answer1() -> float:
    return 0.25
