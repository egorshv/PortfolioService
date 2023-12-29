from datetime import datetime

import pytest
from fastapi.encoders import jsonable_encoder

from schemas.currency import Currency
from schemas.portfolio import PortfolioSchema
from tests.routes.utils import clear_portfolio_db, clear_state_db, clear_trade_db
from settings import TEST


@pytest.mark.asyncio
async def test_update_portfolio_route(
        test_client, test_updating_portfolio_data):
    assert TEST
    await clear_portfolio_db()
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
    await clear_portfolio_db()
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
    await clear_portfolio_db()
    response = test_client.post('/portfolio', json=test_posting_portfolio.model_dump())
    assert response.status_code == 200

    assert response.json() == test_posting_portfolio.model_dump()


@pytest.mark.asyncio
async def test_get_portfolios_by_user_id(test_client, test_posting_portfolio):
    assert TEST
    await clear_portfolio_db()
    response = test_client.post('/portfolio', json=test_posting_portfolio.model_dump())
    assert response.status_code == 200

    response = test_client.get(f'/portfolio?user_id={test_posting_portfolio.user_id}')
    assert response.status_code == 200

    portfolios = list(response.json())
    assert test_posting_portfolio.model_dump() in portfolios


@pytest.mark.asyncio
async def test_get_current_precision(test_client,
                                     test_portfolio_precision,
                                     test_trades_precision,
                                     test_precision_answer):
    assert TEST
    await clear_portfolio_db()
    await clear_trade_db()

    response = test_client.post('/portfolio', json=jsonable_encoder(test_portfolio_precision))
    assert response.status_code == 200

    for trade in test_trades_precision:
        response = test_client.post('/trade', json=jsonable_encoder(trade))
        assert response.status_code == 200

    response = test_client.get(f'/portfolio/{test_portfolio_precision.id}/current_precision')
    assert response.status_code == 200
    print(response.json())
    assert response.json()['last_precision'] == test_precision_answer


@pytest.mark.asyncio
async def test_get_current_recall(test_client,
                                  test_portfolio_recall,
                                  test_recall_trades,
                                  test_recall_answer):
    assert TEST
    await clear_portfolio_db()
    await clear_trade_db()

    response = test_client.post('/portfolio', json=jsonable_encoder(test_portfolio_recall))
    assert response.status_code == 200

    for trade in test_recall_trades:
        response = test_client.post('/trade', json=jsonable_encoder(trade))
        assert response.status_code == 200

    response = test_client.get(f'/portfolio/{test_portfolio_recall.id}/current_recall')
    assert response.status_code == 200
    print(response.json())
    assert response.json()['last_recall'] == test_recall_answer


@pytest.mark.asyncio
async def test_get_chart_data(test_client,
                              test_portfolio_chart_data,
                              test_chart_data_states):
    assert TEST
    await clear_portfolio_db()
    await clear_state_db()

    response = test_client.post('/portfolio', json=jsonable_encoder(test_portfolio_chart_data))
    assert response.status_code == 200

    for state in test_chart_data_states:
        response = test_client.post('/state', json=jsonable_encoder(state))
        assert response.status_code == 200

    response = test_client.get(f'/portfolio/{test_portfolio_chart_data.id}/chart_data?currency={Currency.RUB}')
    assert response.status_code == 200

    chart_data = response.json()[str(test_portfolio_chart_data.id)]
    assert len(chart_data) == len(test_chart_data_states)
    for value, dt in chart_data:
        assert isinstance(value, float)
        assert isinstance(dt, str)
