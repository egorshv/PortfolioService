import pytest

from database.DBCore import DBCore
from database.dao.BaseDAO import BaseDAO
from database.models.portfolio import Portfolio
from schemas.portfolio import PortfolioSchema


@pytest.mark.asyncio
async def test_portfolio_inserting(test_inserting_portfolio):
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_inserting_portfolio)
    getting_portfolio = await dao._get(test_inserting_portfolio.id)

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_deleting_portfolio)
    await dao._delete(test_deleting_portfolio.id)
    portfolios = await dao._list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    await dao._create(test_updating_portfolio)
    updated_portfolio = await dao._update(test_updating_portfolio.id, name='new portfolio name')

    assert updated_portfolio.name == 'new portfolio name'

@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    session = await DBCore().get_session()
    dao = BaseDAO(session, Portfolio, PortfolioSchema)
    await dao._delete_all()

    for portfolio in test_portfolio_list:
        await dao._create(portfolio)

    portfolio_list = await dao._list(user_id=test_portfolio_list[0].user_id)
    assert len(portfolio_list) == len(test_portfolio_list)


@pytest.mark.skip(reason='not implemented')
@pytest.mark.asyncio
async def test_cascade_deleting():
    session = await DBCore().get_session()
