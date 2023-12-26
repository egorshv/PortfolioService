import asyncio
from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession

from database.models.trade import Trade
from database.dao.BaseDAO import BaseDAO
from schemas.trade import TradeSchema


class TradeDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Trade, TradeSchema)

    async def add(self, trade: TradeSchema) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._create(trade)

    async def delete(self, trade_id: int) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(trade_id)

    async def get(self, trade_id: int) -> Optional[TradeSchema]:
        return await self._get(trade_id)

    async def update(self, trade_id: int, **kwargs) -> Optional[TradeSchema]:
        lock = asyncio.Lock()
        async with lock:
            return await self._update(trade_id, **kwargs)

    async def list(self, **kwargs) -> Optional[List[TradeSchema]]:
        return await self._list(**kwargs)

    async def delete_all(self) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete_all()
