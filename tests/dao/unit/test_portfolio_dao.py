import pytest

from database.MongoClientSingleton import MongoClientSingleton
from database.dao.PortfolioDAO import PortfolioDAO
from settings import MONGO_DB


@pytest.mark.asyncio
async def test_portfolio_dao_inserting(test_inserting_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = PortfolioDAO(client, MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_inserting_portfolio)
    getting_portfolio = await dao.get(
        test_inserting_portfolio.name,
        test_inserting_portfolio.user_id
    )

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = PortfolioDAO(client, MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_deleting_portfolio)
    await dao.delete(test_deleting_portfolio.name, test_deleting_portfolio.user_id)
    portfolios = await dao.list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = PortfolioDAO(client, MONGO_DB['TEST_COLLECTION'])

    await dao.add(test_updating_portfolio)
    updated_portfolio = await dao.update(
        test_updating_portfolio.name,
        test_updating_portfolio.user_id,
        name='new portfolio name'
    )

    assert updated_portfolio.name == 'new portfolio name'


@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    client = MongoClientSingleton(MONGO_DB_HOST, MONGO_DB_PORT)
    dao = PortfolioDAO(client, TEST_MONGO_DB_COLLECTION)

    await dao.delete_many()

    for portfolio in test_portfolio_list:
        await dao.add(portfolio)

    portfolio_list = await dao.list()

    assert portfolio_list == test_portfolio_list
