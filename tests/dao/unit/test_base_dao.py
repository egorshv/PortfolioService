import pytest

from database.MongoClientSingleton import MongoClientSingleton
from database.dao.BaseDAO import BaseDAO
from schemas.portfolio import Portfolio
from settings import MONGO_DB


@pytest.mark.asyncio
async def test_portfolio_inserting(test_inserting_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = BaseDAO(client, MONGO_DB['COLLECTION'], Portfolio)

    await dao._add(test_inserting_portfolio)
    getting_portfolio = await dao._get(name=test_inserting_portfolio.name)

    assert test_inserting_portfolio == getting_portfolio


@pytest.mark.asyncio
async def test_portfolio_deleting(test_deleting_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = BaseDAO(client, MONGO_DB['COLLECTION'], Portfolio)

    await dao._add(test_deleting_portfolio)
    await dao._delete(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)
    portfolios = await dao._list(name=test_deleting_portfolio.name, user_id=test_deleting_portfolio.user_id)

    assert portfolios == []


@pytest.mark.asyncio
async def test_portfolio_updating(test_updating_portfolio):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = BaseDAO(client, MONGO_DB['COLLECTION'], Portfolio)

    await dao._add(test_updating_portfolio)
    updated_portfolio = await dao._update(
        {'name': test_updating_portfolio.name,
         'user_id': test_updating_portfolio.user_id},
        name='new portfolio name'
    )

    assert updated_portfolio.name == 'new portfolio name'


@pytest.mark.asyncio
async def test_portfolio_list(test_portfolio_list):
    client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
    dao = BaseDAO(client, MONGO_DB['COLLECTION'], Portfolio)

    await dao._delete_many()

    for portfolio in test_portfolio_list:
        await dao._add(portfolio)

    portfolio_list = await dao._list()

    assert portfolio_list == test_portfolio_list
