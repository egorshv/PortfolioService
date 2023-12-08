import asyncio
from typing import List, Optional

from database.dao.BaseDAO import BaseDAO
from database.MongoClientSingleton import MongoClientSingleton
from schemas.portfolio import Portfolio


class PortfolioDAO(BaseDAO):
    def __init__(self, client: MongoClientSingleton, collection_name: str):
        super().__init__(client, collection_name, Portfolio)

    async def add(self, portfolio: Portfolio) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._add(portfolio)

    async def delete(self, portfolio_name: str, user_id: int) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(name=portfolio_name, user_id=user_id)

    async def get(self, portfolio_name: str, user_id: int) -> Optional[Portfolio]:
        return await self._get(name=portfolio_name, user_id=user_id)

    async def update(self, portfolio_name: str, user_id: int, **kwargs) -> Optional[Portfolio]:
        lock = asyncio.Lock()
        async with lock:
            return await self._update({'name': portfolio_name, 'user_id': user_id}, **kwargs)

    async def list(self, **kwargs) -> Optional[List[Portfolio]]:
        return await self._list(**kwargs)

    async def delete_many(self, **kwargs):
        await self._delete_many(**kwargs)
