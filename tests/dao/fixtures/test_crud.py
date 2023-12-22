from datetime import datetime

import pytest

from schemas.portfolio import Portfolio
from schemas.state import State
from schemas.trade import Trade, TradeActionType
from schemas.currency import Currency


@pytest.fixture
def test_inserting_portfolio():
    return Portfolio(
        name='main_portfolio',
        user_id=1
    )


@pytest.fixture
def test_deleting_portfolio():
    return Portfolio(
        name='deleting_portfolio',
        user_id=2
    )


@pytest.fixture
def test_updating_portfolio():
    return Portfolio(
        name='old portfolio name',
        user_id=3
    )


@pytest.fixture
def test_portfolio_names():
    return [f'Name {i}' for i in range(10)]


@pytest.fixture
def test_portfolio_list(test_portfolio_names):
    return [
        Portfolio(
            name=name,
            user_id=_id
        )
        for _id, name in enumerate(test_portfolio_names)
    ]


@pytest.fixture
def test_portfolio():
    return Portfolio(
        name='portfolio 1',
        user_id=4
    )


@pytest.fixture
def test_portfolio_with_same_name():
    return Portfolio(
        name='portfolio 1',
        user_id=4
    )


@pytest.fixture
def test_portfolio1():
    return Portfolio(
        name='portfolio 2',
        user_id=5
    )
