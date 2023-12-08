import pytest

from database.dao.PortfolioDAO import PortfolioDAO
from settings import MONGO_DB


@pytest.mark.asyncio
async def test_portfolio_dao_inserting(test_inserting_portfolio):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_inserting_portfolio)
    getting_portfolio = await dao.get(
        test_inserting_portfolio.name,
        test_inserting_portfolio.user_id
    )

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_deleting_portfolio)
    await dao.delete(test_deleting_portfolio.name, test_deleting_portfolio.user_id)
    portfolios = await dao.list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_updating_portfolio)
    updated_portfolio = await dao.update(
        test_updating_portfolio.name,
        test_updating_portfolio.user_id,
        name='new portfolio name'
    )

    assert updated_portfolio.name == 'new portfolio name'


@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])

    await dao.delete_many()

    for portfolio in test_portfolio_list:
        await dao.add(portfolio)

    portfolio_list = await dao.list()

    assert portfolio_list == test_portfolio_list


@pytest.mark.asyncio
async def test_add_trade(test_portfolio, test_trade, test_trade1):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])
    await dao.delete_many()
    await dao.add(test_portfolio)
    await dao.add_trade(test_trade, test_portfolio.name, test_portfolio.user_id)
    await dao.add_trade(test_trade1, test_portfolio.name, test_portfolio.user_id)

    portfolio = await dao.get(test_portfolio.name, test_portfolio.user_id)
    assert len(portfolio.trades) == 2


@pytest.mark.asyncio
async def test_add_state(test_portfolio1, test_state, test_state1):
    dao = PortfolioDAO(MONGO_DB['TEST_COLLECTION'])
    await dao.delete_many()
    await dao.add(test_portfolio1)
    await dao.add_state(test_state, test_portfolio1.name, test_portfolio1.user_id)
    await dao.add_state(test_state1, test_portfolio1.name, test_portfolio1.user_id)

    portfolio = await dao.get(test_portfolio1.name, test_portfolio1.user_id)
    assert len(portfolio.states) == 2
