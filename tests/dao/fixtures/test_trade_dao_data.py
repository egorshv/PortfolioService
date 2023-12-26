from datetime import datetime
from typing import List

import pytest

from schemas.trade import TradeSchema, TradeActionType, Currency


@pytest.fixture
def test_inserting_trade() -> TradeSchema:
    return TradeSchema(
        id=1,
        portfolio_id=1,
        ticker='abcd',
        action=TradeActionType.BUY,
        value=100,
        currency=Currency.USD,
        created_at=datetime.now(),
    )


@pytest.fixture
def test_deleting_trade() -> TradeSchema:
    return TradeSchema(
        id=2,
        portfolio_id=1,
        ticker='abcd',
        action=TradeActionType.SELL,
        value=130,
        currency=Currency.USD,
        created_at=datetime.now(),
    )


@pytest.fixture
def test_updating_trade() -> TradeSchema:
    return TradeSchema(
        id=3,
        portfolio_id=1,
        ticker='abcd',
        action=TradeActionType.BUY,
        value=330,
        currency=Currency.RUB,
        created_at=datetime.now(),
    )


@pytest.fixture
def test_trade_list() -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 4,
            portfolio_id=4,
            ticker='abcd',
            action=TradeActionType.BUY,
            value=330,
            currency=Currency.RUB,
            created_at=datetime.now(),
        )
        for i in range(10)
    ]
