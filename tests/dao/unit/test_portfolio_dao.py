import pytest

from database.DBCore import DBCore
from database.dao.PortfolioDAO import PortfolioDAO
from settings import TEST


@pytest.mark.asyncio
async def test_portfolio_dao_inserting(test_inserting_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()

    await dao.add(test_inserting_portfolio)
    getting_portfolio = await dao.get(
        test_inserting_portfolio.id
    )

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()

    await dao.add(test_deleting_portfolio)
    await dao.delete(test_deleting_portfolio.id)
    portfolios = await dao.list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    assert TEST
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()

    await dao.add(test_updating_portfolio)
    updated_portfolio = await dao.update(
        test_updating_portfolio.id,
        name='new portfolio name'
    )

    assert updated_portfolio.name == 'new portfolio name'


@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    assert TEST
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()

    for portfolio in test_portfolio_list:
        await dao.add(portfolio)

    portfolio_list = await dao.list()

    assert portfolio_list == test_portfolio_list
