import pytest

from database.DBCore import DBCore
from database.dao.TradeDAO import TradeDAO
from settings import TEST


@pytest.mark.asyncio
async def test_trade_inserting(test_inserting_trade):
    assert TEST
    session = await DBCore().get_session()
    dao = TradeDAO(session)
    await dao.delete_all()

    await dao.add(test_inserting_trade)
    getting_trade = await dao.get(test_inserting_trade.id)
    assert test_inserting_trade == getting_trade


@pytest.mark.asyncio
async def test_trade_deleting(test_deleting_trade):
    assert TEST
    session = await DBCore().get_session()
    dao = TradeDAO(session)
    await dao.delete_all()

    await dao.add(test_deleting_trade)
    await dao.delete(test_deleting_trade.id)
    getting_trade = await dao.get(test_deleting_trade.id)
    assert getting_trade is None


@pytest.mark.asyncio
async def test_trade_updating(test_updating_trade):
    assert TEST
    session = await DBCore().get_session()
    dao = TradeDAO(session)
    await dao.delete_all()

    ticker = 'SBER'

    await dao.add(test_updating_trade)
    updated_trade = await dao.update(test_updating_trade.id, ticker=ticker)
    assert updated_trade.ticker == ticker


@pytest.mark.asyncio
async def test_list_of_trades(test_trade_list):
    assert TEST
    session = await DBCore().get_session()
    dao = TradeDAO(session)
    await dao.delete_all()

    for trade in test_trade_list:
        await dao.add(trade)

    trade_list = await dao.list(portfolio_id=4)
    assert trade_list == test_trade_list
