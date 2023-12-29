from datetime import datetime

import pytest

from schemas.currency import Currency
from schemas.operation import OperationSchema
from schemas.portfolio import PortfolioSchema
from schemas.state import StateSchema
from schemas.trade import TradeSchema, TradeActionType


@pytest.fixture
def test_inserting_portfolio():
    return PortfolioSchema(
        id=1,
        name='main_portfolio',
        user_id=1
    )


@pytest.fixture
def test_deleting_portfolio():
    return PortfolioSchema(
        id=2,
        name='deleting_portfolio',
        user_id=2
    )


@pytest.fixture
def test_updating_portfolio():
    return PortfolioSchema(
        id=3,
        name='old portfolio name',
        user_id=3
    )


@pytest.fixture
def test_portfolio_names():
    return [f'Name {i}' for i in range(10)]


@pytest.fixture
def test_portfolio_list(test_portfolio_names):
    return [
        PortfolioSchema(
            id=_id + 3,
            name=name,
            user_id=256
        )
        for _id, name in enumerate(test_portfolio_names)
    ]


@pytest.fixture
def test_portfolio():
    return PortfolioSchema(
        id=13,
        name='portfolio 1',
        user_id=4
    )


@pytest.fixture
def test_portfolio1():
    return PortfolioSchema(
        id=15,
        name='portfolio 2',
        user_id=5
    )


@pytest.fixture
def test_states():
    return [
        StateSchema(
            id=i + 1,
            portfolio_id=1,
            usd_result=0,
            rub_result=0,
            created_at=datetime.now()
        )
        for i in range(10)
    ]


@pytest.fixture
def test_operations():
    return [
        OperationSchema(
            id=i + 1,
            portfolio_id=1,
            value=0,
            created_at=datetime.now()
        )
        for i in range(10)
    ]


@pytest.fixture
def test_trades():
    return [
        TradeSchema(
            id=i + 1,
            portfolio_id=1,
            ticker='SBER',
            action=TradeActionType.BUY,
            value=0,
            currency=Currency.RUB,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
