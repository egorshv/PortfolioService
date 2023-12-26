import pytest

from database import DBCore
from database.dao.PortfolioDAO import PortfolioDAO
from schemas.portfolio import PortfolioSchema
from settings import TEST


async def clear_db():
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()


@pytest.mark.asyncio
async def test_update_portfolio_route(
        test_client, test_updating_portfolio_data):
    assert TEST
    await clear_db()
    portfolio, new_portfolio_name = test_updating_portfolio_data
    add_response = test_client.post('/portfolio', json=portfolio.model_dump())
    assert add_response.status_code == 200

    new_portfolio = PortfolioSchema(
        id=portfolio.id,
        name=new_portfolio_name,
        user_id=portfolio.user_id
    )
    response = test_client.put(f'portfolio/{portfolio.id}', json=new_portfolio.model_dump())
    assert response.status_code == 200

    get_response = test_client.get(f'portfolio/{new_portfolio.id}')
    assert get_response.status_code == 200

    updated_portfolio = PortfolioSchema(**get_response.json())
    assert updated_portfolio.name == new_portfolio_name


@pytest.mark.asyncio
async def test_delete_portfolio_route(test_client, test_deleting_portfolio):
    assert TEST
    await clear_db()
    add_response = test_client.post(f'/portfolio', json=test_deleting_portfolio.model_dump())
    assert add_response.status_code == 200

    response = test_client.delete(f'/portfolio/{test_deleting_portfolio.id}')
    assert response.status_code == 200

    get_response = test_client.get(f'/portfolio/{test_deleting_portfolio.id}')
    assert get_response.status_code == 200
    assert get_response.json() is None


@pytest.mark.asyncio
async def test_post_portfolio_route(test_client, test_posting_portfolio):
    assert TEST
    await clear_db()
    response = test_client.post('/portfolio', json=test_posting_portfolio.model_dump())
    assert response.status_code == 200

    assert response.json() == test_posting_portfolio.model_dump()


@pytest.mark.asyncio
async def test_get_portfolios_by_user_id(test_client, test_posting_portfolio):
    assert TEST
    await clear_db()
    response = test_client.post('/portfolio', json=test_posting_portfolio.model_dump())
    assert response.status_code == 200

    response = test_client.get(f'/portfolios?user_id={test_posting_portfolio.user_id}')
    assert response.status_code == 200

    portfolios = list(response.json())
    assert test_posting_portfolio.model_dump() in portfolios
