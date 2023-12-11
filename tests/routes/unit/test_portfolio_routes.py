import pytest

from schemas.portfolio import Portfolio


@pytest.mark.asyncio
async def test_get_portfolio_route(test_client, test_portfolio_data):
    user_id, portfolio_name = test_portfolio_data
    response = test_client.get(f'/portfolio/{user_id}/{portfolio_name}')
    assert response.status_code == 200

    portfolio = Portfolio(**response.json())
    assert portfolio.name == portfolio_name


@pytest.mark.asyncio
async def test_get_portfolios_by_user_id(test_client, test_portfolio_data):
    user_id, _ = test_portfolio_data
    response = test_client.get(f'/portfolios?user_id={user_id}')
    assert response.status_code == 200

    portfolios = list(response.json())
    assert len(portfolios) == 2


@pytest.mark.asyncio
async def test_get_portfolios_by_portfolio_name(test_client, test_portfolio_data):
    _, portfolio_name = test_portfolio_data
    response = test_client.get(f'/portfolios?name={portfolio_name}')
    assert response.status_code == 200

    portfolios = list(response.json())
    assert len(portfolios) == 1


@pytest.mark.asyncio
async def test_update_portfolio_route(
        test_client, test_updating_portfolio_data):
    portfolio, new_portfolio_name = test_updating_portfolio_data
    add_response = test_client.post('/portfolio/post', json=portfolio.model_dump())
    assert add_response.status_code == 200

    new_portfolio = Portfolio(
        name=new_portfolio_name,
        user_id=portfolio.user_id
    )
    response = test_client.put(f'portfolio/put/{portfolio.user_id}/{portfolio.name}', json=new_portfolio.model_dump())
    assert response.status_code == 200

    updated_portfolio = Portfolio(**response.json())
    assert updated_portfolio.name == new_portfolio_name


@pytest.mark.asyncio
async def test_delete_portfolio_route(test_client, test_deleting_portfolio):
    add_response = test_client.post(f'/portfolio/post', json=test_deleting_portfolio.model_dump())
    assert add_response.status_code == 200

    response = test_client.delete(f'/portfolio/delete/{test_deleting_portfolio.user_id}/{test_deleting_portfolio.name}')
    assert response.status_code == 200

    get_response = test_client.get(f'/portfolios?user_id={test_deleting_portfolio.user_id}')
    assert get_response.status_code == 200
    assert len(list(get_response.json())) == 0


@pytest.mark.asyncio
async def test_post_portfolio_route(test_client, test_posting_portfolio):
    response = test_client.post('/portfolio/post', json=test_posting_portfolio.model_dump())
    assert response.status_code == 200

    assert response.json() == test_posting_portfolio.model_dump()
