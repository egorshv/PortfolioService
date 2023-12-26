import pytest
from fastapi.testclient import TestClient

from app import app
from schemas.portfolio import PortfolioSchema


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
