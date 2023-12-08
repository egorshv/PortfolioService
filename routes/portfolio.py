from typing import List

from fastapi import APIRouter

from database.dao.PortfolioDAO import PortfolioDAO
from schemas.portfolio import Portfolio
from schemas.state import State
from schemas.trade import Trade
from settings import MONGO_DB

portfolio_router = APIRouter()


@portfolio_router.get('/portfolio', response_model=List[Portfolio])
async def get_portfolios(name: str = None, user_id: int = None) -> List[Portfolio]:
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    portfolios = await dao.list(name=name, user_id=user_id)
    return portfolios


@portfolio_router.get('/portfolio_states', response_model=List[State])
async def get_portfolio_states(name: str, user_id: int) -> List[State]:
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    portfolio = await dao.get(name, user_id)
    return portfolio.states


@portfolio_router.get('/portfolio_trades', response_model=List[Trade])
async def get_portfolio_trades(name: str, user_id: int):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    portfolio = await dao.get(name, user_id)
    return portfolio.trades


@portfolio_router.post('/portfolio/add_trade')
async def post_trade(trade: Trade, portfolio_name: str, user_id: int):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    await dao.add_trade(trade, portfolio_name, user_id)


@portfolio_router.post('/portfolio/add_state')
async def post_state(state: State, portfolio_name: str, user_id: int):
    dao = PortfolioDAO(MONGO_DB['COLLECTION'])
    await dao.add_state(state, portfolio_name, user_id)
