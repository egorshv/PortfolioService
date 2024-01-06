import pytest

from database.DBCore import DBCore
from database.dao.BaseDAO import BaseDAO
from database.dao.OperationDAO import OperationDAO
from database.dao.PortfolioDAO import PortfolioDAO
from database.dao.StateDAO import StateDAO
from database.dao.TradeDAO import TradeDAO
from database.models.portfolio import Portfolio
from schemas.portfolio import PortfolioSchema
from settings import TEST


@pytest.mark.asyncio
async def test_portfolio_inserting(test_inserting_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_inserting_portfolio)
    getting_portfolio = await dao._get(test_inserting_portfolio.id)

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_deleting_portfolio)
    await dao._delete(test_deleting_portfolio.id)
    portfolios = await dao._list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_updating_portfolio)
    updated_portfolio = await dao._update(test_updating_portfolio.id, name='new portfolio name')

    assert updated_portfolio.name == 'new portfolio name'


@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    assert TEST
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    for portfolio in test_portfolio_list:
        await dao._create(portfolio)

    portfolio_list = await dao._list(user_id=test_portfolio_list[0].user_id)
    assert len(portfolio_list) == len(test_portfolio_list)


@pytest.mark.skip(reason='works only with prod database')
@pytest.mark.asyncio
async def test_cascade_deleting(test_inserting_portfolio, test_trades, test_operations, test_states):
    session = await DBCore().get_session()
    portfolio_dao = PortfolioDAO(session)
    trade_dao = TradeDAO(session)
    operation_dao = OperationDAO(session)
    state_dao = StateDAO(session)

    [await dao.delete_all() for dao in [portfolio_dao, operation_dao, state_dao, trade_dao]]

    await portfolio_dao.add(test_inserting_portfolio)
    getting_portfolio = await portfolio_dao.get(test_inserting_portfolio.id)
    assert getting_portfolio.id == 1

    [await state_dao.add(state) for state in test_states]
    [await operation_dao.add(operation) for operation in test_operations]
    [await trade_dao.add(trade) for trade in test_trades]

    getting_states = await state_dao.list()
    assert len(getting_states) == len(test_states)

    getting_operations = await state_dao.list()
    assert len(getting_operations) == len(test_operations)

    getting_trades = await trade_dao.list()
    assert len(getting_trades) == len(test_trades)

    await portfolio_dao.delete(test_inserting_portfolio.id)
    states = await state_dao.list(portfolio_id=test_inserting_portfolio.id)
    trades = await trade_dao.list(portfolio_id=test_inserting_portfolio.id)
    operations = await operation_dao.list(portfolio_id=test_inserting_portfolio.id)

    assert states == []
    assert trades == []
    assert operations == []
