import asyncio
import uuid
from typing import List

from BaseDAO import BaseDAO
from MongoClientSingleton import MongoClientSingleton
from schemas.portfolio import Portfolio


class PortfolioDAO(BaseDAO):
    def __init__(self, client: MongoClientSingleton):
        super().__init__(client, 'portfolio', Portfolio)

    async def add(self, portfolio: Portfolio) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._add(portfolio)

    async def delete(self, portfolio_id: uuid.UUID) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(portfolio_id)

    async def get(self, portfolio_id: uuid.UUID) -> Portfolio:
        return await self._get(portfolio_id)

    async def update(self, portfolio_id: uuid.UUID, **kwargs) -> Portfolio:
        lock = asyncio.Lock()
        async with lock:
            return await self._update(portfolio_id, **kwargs)

    async def list(self, **kwargs) -> List[Portfolio]:
        return await self._list(**kwargs)

