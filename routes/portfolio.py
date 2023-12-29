from typing import List, Optional, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.PortfolioDAO import PortfolioDAO
from database.dao.StateDAO import StateDAO
from database.dao.TradeDAO import TradeDAO
from routes.utils import get_async_session
from schemas.currency import Currency
from schemas.portfolio import PortfolioSchema
from schemas.state import StateSchema
from schemas.trade import TradeSchema
from services.PortfolioHandler import PortfolioHandler

portfolio_router = APIRouter()


@portfolio_router.get('/portfolio', response_model=List[PortfolioSchema])
async def get_portfolios(user_id: int = None, session: AsyncSession = Depends(get_async_session)) -> \
        List[PortfolioSchema]:
    dao = PortfolioDAO(session)
    portfolios = await dao.list(user_id=user_id)
    return portfolios


@portfolio_router.get('/portfolio/{portfolio_id}', response_model=Optional[PortfolioSchema])
async def get_portfolio(portfolio_id, session: AsyncSession = Depends(get_async_session)) -> Optional[PortfolioSchema]:
    dao = PortfolioDAO(session)
    portfolio = await dao.get(portfolio_id)
    return portfolio


@portfolio_router.post('/portfolio', response_model=Optional[PortfolioSchema])
async def post_portfolio(portfolio: PortfolioSchema,
                         session: AsyncSession = Depends(get_async_session)) -> Optional[PortfolioSchema]:
    dao = PortfolioDAO(session)
    created_portfolio = await dao.add(portfolio)
    return created_portfolio


@portfolio_router.delete('/portfolio/{portfolio_id}')
async def delete_portfolio(portfolio_id: int, session: AsyncSession = Depends(get_async_session)):
    dao = PortfolioDAO(session)
    await dao.delete(portfolio_id)
    return {'result': 'portfolio deleted'}


@portfolio_router.put('/portfolio/{portfolio_id}', response_model=Optional[PortfolioSchema])
async def update_portfolio(portfolio_id: int, new_portfolio: PortfolioSchema,
                           session: AsyncSession = Depends(get_async_session)) -> Optional[PortfolioSchema]:
    dao = PortfolioDAO(session)
    updated_portfolio = await dao.update(portfolio_id, **new_portfolio.model_dump())
    return updated_portfolio


@portfolio_router.get('/portfolio/{portfolio_id}/current_recall', response_model=PortfolioSchema)
async def get_current_recall(portfolio_id: int, session: AsyncSession = Depends(get_async_session)) -> PortfolioSchema:
    portfolio_handler = PortfolioHandler()
    trades: List[TradeSchema] = await TradeDAO(session).list(portfolio_id=portfolio_id)
    current_recall = portfolio_handler.eval_recall(trades)
    return await PortfolioDAO(session).update(portfolio_id, last_recall=current_recall)


@portfolio_router.get('/portfolio/{portfolio_id}/current_precision', response_model=PortfolioSchema)
async def get_current_precision(portfolio_id: int,
                                session: AsyncSession = Depends(get_async_session)) -> PortfolioSchema:
    portfolio_handler = PortfolioHandler()
    trades = await TradeDAO(session).list(portfolio_id=portfolio_id)
    current_precision = portfolio_handler.eval_precision(trades)
    return await PortfolioDAO(session).update(portfolio_id, last_precision=current_precision)


@portfolio_router.get('/portfolio/{portfolio_id}/chart_data')
async def get_chart_data(portfolio_id: int, currency: Currency,
                         session: AsyncSession = Depends(get_async_session)):
    portfolio_handler = PortfolioHandler()
    states = await StateDAO(session).list(portfolio_id=portfolio_id)
    chart_data = portfolio_handler.get_chart_data(states, currency)
    return {portfolio_id: chart_data}
