import pytest

from schemas.trade import TradeSchema
from settings import TEST
from tests.routes.utils import clear_trade_db
from fastapi.encoders import jsonable_encoder


@pytest.mark.asyncio
async def test_post_trade(test_client, test_posting_trade):
    assert TEST
    await clear_trade_db()

    post_response = test_client.post('/trade', json=jsonable_encoder(test_posting_trade))
    assert post_response.status_code == 200

    assert post_response.json() == jsonable_encoder(test_posting_trade)


@pytest.mark.asyncio
async def test_get_trade(test_client, test_getting_trade):
    assert TEST
    await clear_trade_db()

    post_response = test_client.post('/trade', json=jsonable_encoder(test_getting_trade))
    assert post_response.status_code == 200

    get_response = test_client.get(f'/trade/{test_getting_trade.id}')
    assert get_response.status_code == 200

    trade = TradeSchema(**get_response.json())
    assert trade == test_getting_trade


@pytest.mark.asyncio
async def test_update_trade(test_client, test_updating_trade, test_updated_trade):
    assert TEST
    await clear_trade_db()

    post_response = test_client.post('/trade', json=jsonable_encoder(test_updating_trade))
    assert post_response.status_code == 200

    update_response = test_client.put(f'/trade/{test_updating_trade.id}', json=jsonable_encoder(test_updated_trade))
    assert update_response.status_code == 200
    assert update_response.json() == jsonable_encoder(test_updated_trade)


@pytest.mark.asyncio
async def test_delete_trade(test_client, test_deleting_trade):
    assert TEST
    await clear_trade_db()

    post_response = test_client.post('/trade', json=jsonable_encoder(test_deleting_trade))
    assert post_response.status_code == 200

    delete_response = test_client.delete(f'/trade/{test_deleting_trade.id}')
    assert delete_response.status_code == 200


@pytest.mark.asyncio
async def test_list_trade(test_client, test_trade_posting_list):
    assert TEST
    await clear_trade_db()

    for trade in test_trade_posting_list:
        post_response = test_client.post('/trade', json=jsonable_encoder(trade))
        assert post_response.status_code == 200

    list_response = test_client.get(f'/trade?portfolio_id={test_trade_posting_list[0].portfolio_id}')
    assert list_response.status_code == 200
    assert list_response.json()[0] == jsonable_encoder(test_trade_posting_list[0])
