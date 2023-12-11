from typing import List

from fastapi import APIRouter

from database.dao.PortfolioDAO import PortfolioDAO
from schemas.portfolio import Portfolio
from settings import MONGO_DB

portfolio_router = APIRouter()


@portfolio_router.get('/portfolios', response_model=List[Portfolio])
async def get_portfolios(name: str = None, user_id: int = None) -> List[Portfolio]:
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    portfolios = await dao.list(name=name, user_id=user_id)
    return portfolios


@portfolio_router.get('/portfolio/{user_id}/{portfolio_name}', response_model=Portfolio)
async def get_portfolio(user_id: int, portfolio_name: str):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    portfolio = await dao.get(portfolio_name, user_id)
    return portfolio


@portfolio_router.post('/portfolio/post', response_model=Portfolio)
async def post_portfolio(portfolio: Portfolio):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    await dao.add(portfolio)
    return portfolio


@portfolio_router.delete('/portfolio/delete/{user_id}/{portfolio_name}')
async def delete_portfolio(user_id: int, portfolio_name: str):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    await dao.delete(portfolio_name, user_id)
    return {'result': 'portfolio deleted'}


@portfolio_router.put('portfolio/put/{user_id}/{portfolio_name}')
async def update_portfolio(user_id: int, portfolio_name: str, new_portfolio: Portfolio):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    await dao.update(portfolio_name, user_id, **new_portfolio.model_dump())
    return {'result': 'portfolio updated'}
