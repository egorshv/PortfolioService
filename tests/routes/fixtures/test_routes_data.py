from datetime import datetime
from typing import List

import pytest
from fastapi.testclient import TestClient

from app.main import app
from schemas.currency import Currency
from schemas.portfolio import PortfolioSchema
from schemas.state import StateSchema
from schemas.trade import TradeSchema, TradeMark, TradeActionType


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def test_getting_portfolio():
    return PortfolioSchema(
        id=255,
        name='getting portfolio',
        user_id=59340,
    )


@pytest.fixture
def test_posting_portfolio():
    return PortfolioSchema(
        id=1,
        name='posting portfolio',
        user_id=254
    )


@pytest.fixture
def test_updating_portfolio_data():
    return PortfolioSchema(
        id=2,
        name='updating portfolio',
        user_id=932
    ), 'updated portfolio name'


@pytest.fixture
def test_deleting_portfolio():
    return PortfolioSchema(
        id=3,
        name='deleting portfolio',
        user_id=1024
    )


@pytest.fixture
def test_portfolio_precision() -> PortfolioSchema:
    return PortfolioSchema(
        id=1,
        name='precision',
        user_id=1024
    )


@pytest.fixture
def test_precision_trademarks() -> List[TradeMark]:
    return [TradeMark.TP] * 10 + [TradeMark.FP] * 40


@pytest.fixture
def test_trades_precision(test_precision_trademarks) -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=1,
            ticker='',
            action=TradeActionType.BUY,
            value=500,
            currency=Currency.USD,
            created_at=datetime.now(),
            mark=mark
        )
        for i, mark in enumerate(test_precision_trademarks)
    ]


@pytest.fixture
def test_precision_answer() -> float:
    return 0.2


@pytest.fixture
def test_portfolio_recall() -> PortfolioSchema:
    return PortfolioSchema(
        id=2,
        name='recall',
        user_id=1024
    )


@pytest.fixture
def test_recall_trademarks() -> List[TradeMark]:
    return [TradeMark.FN] * 3 + [TradeMark.TP]


@pytest.fixture
def test_recall_trades(test_recall_trademarks) -> List[TradeSchema]:
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=2,
            ticker='',
            action=TradeActionType.BUY,
            value=500,
            currency=Currency.USD,
            created_at=datetime.now(),
            mark=mark
        )
        for i, mark in enumerate(test_recall_trademarks)
    ]


@pytest.fixture
def test_recall_answer() -> float:
    return 0.25


@pytest.fixture
def test_portfolio_chart_data() -> PortfolioSchema:
    return PortfolioSchema(
        id=3,
        name='chart',
        user_id=1024
    )


@pytest.fixture
def test_chart_data_states() -> List[StateSchema]:
    return [
        StateSchema(
            id=i + 1,
            portfolio_id=3,
            usd_result=15 + i,
            rub_result=22 + i * 3 - 12,
            created_at=datetime.now()
        )
        for i in range(20)
    ]
