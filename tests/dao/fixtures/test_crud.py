import pytest

from database.DBCore import DBCore
from schemas.portfolio import PortfolioSchema


@pytest.fixture
async def test_session():
    core = DBCore()
    session = await core.get_session()
    return session


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
