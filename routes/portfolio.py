from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.PortfolioDAO import PortfolioDAO
from routes.utils import get_async_session
from schemas.portfolio import PortfolioSchema

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
