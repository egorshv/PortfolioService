from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.TradeDAO import TradeDAO
from routes.utils import get_async_session
from schemas.currency import Currency
from schemas.trade import TradeSchema, TradeActionType, TradeMark

trade_router = APIRouter()


@trade_router.get('/trade/{trade_id}', response_model=Optional[TradeSchema])
async def get_trade(trade_id: int, session: AsyncSession = Depends(get_async_session)) -> TradeSchema:
    dao = TradeDAO(session)
    trade = await dao.get(trade_id)
    return trade


@trade_router.get('/trade', response_model=List[TradeSchema])
async def get_trades(portfolio_id: int = None, ticker: str = None, action: TradeActionType = None,
                     value: int = None, currency: Currency = None, mark: TradeMark = None,
                     session: AsyncSession = Depends(get_async_session)) -> List[TradeSchema]:
    dao = TradeDAO(session)
    trades = await dao.list(
        portfolio_id=portfolio_id,
        ticker=ticker,
        action=action,
        value=value,
        currency=currency,
        mark=mark
    )
    return trades


@trade_router.post('/trade', response_model=Optional[TradeSchema])
async def post_trade(trade: TradeSchema, session: AsyncSession = Depends(get_async_session)) -> Optional[TradeSchema]:
    dao = TradeDAO(session)
    return await dao.add(trade)


@trade_router.delete('/trade/{trade_id}')
async def delete_trade(trade_id: int, session: AsyncSession = Depends(get_async_session)):
    dao = TradeDAO(session)
    await dao.delete(trade_id)
    return {'result': 'trade deleted'}


@trade_router.put('/trade/{trade_id}', response_model=Optional[TradeSchema])
async def update_trade(trade_id: int, new_trade: TradeSchema,
                       session: AsyncSession = Depends(get_async_session)) -> Optional[TradeSchema]:
    dao = TradeDAO(session)
    return await dao.update(trade_id, **new_trade.model_dump())


