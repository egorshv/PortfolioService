from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.PortfolioDAO import PortfolioDAO
from schemas.portfolio import PortfolioSchema
from routes.utils import get_async_session

portfolio_router = APIRouter()


@portfolio_router.get('/portfolios', response_model=List[PortfolioSchema])
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
    await dao.add(portfolio)
    return portfolio


@portfolio_router.delete('/portfolio/{portfolio_id}')
async def delete_portfolio(portfolio_id: int, session: AsyncSession = Depends(get_async_session)):
    dao = PortfolioDAO(session)
    await dao.delete(portfolio_id)
    return {'result': 'portfolio deleted'}


@portfolio_router.put('/portfolio/{portfolio_id}', response_model=Optional[PortfolioSchema])
async def update_portfolio(portfolio_id: int, new_portfolio: PortfolioSchema,
                           session: AsyncSession = Depends(get_async_session)) -> Optional[PortfolioSchema]:
    dao = PortfolioDAO(session)
    return await dao.update(portfolio_id, **new_portfolio.model_dump())
