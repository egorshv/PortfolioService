from datetime import datetime
from typing import List

import pytest

from schemas.currency import Currency
from schemas.trade import TradeSchema, TradeActionType


@pytest.fixture
def test_getting_trade() -> TradeSchema:
    return TradeSchema(
        id=1,
        portfolio_id=1,
        ticker='',
        action=TradeActionType.SELL,
        value=100,
        currency=Currency.USD,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updating_trade() -> TradeSchema:
    return TradeSchema(
        id=2,
        portfolio_id=1,
        ticker='',
        action=TradeActionType.BUY,
        value=300,
        currency=Currency.USD,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updated_trade() -> TradeSchema:
    return TradeSchema(
        id=2,
        portfolio_id=4,
        ticker='TICKER',
        action=TradeActionType.SELL,
        value=350,
        currency=Currency.USD,
        created_at=datetime.now()
    )


@pytest.fixture
def test_posting_trade() -> TradeSchema:
    return TradeSchema(
        id=3,
        portfolio_id=1,
        ticker='YNDX',
        action=TradeActionType.BUY,
        value=2500,
        currency=Currency.RUB,
        created_at=datetime.now()
    )


@pytest.fixture
def test_deleting_trade() -> TradeSchema:
    return TradeSchema(
        id=4,
        portfolio_id=1,
        ticker='LKOH',
        action=TradeActionType.BUY,
        value=7000,
        currency=Currency.RUB,
        created_at=datetime.now()
    )


@pytest.fixture
def test_trade_posting_list() -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=i + 70,
            ticker='LKOH',
            action=TradeActionType.BUY,
            value=7000,
            currency=Currency.RUB,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
