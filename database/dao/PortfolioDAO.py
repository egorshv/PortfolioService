import asyncio
from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.BaseDAO import BaseDAO
from database.models.portfolio import Portfolio
from schemas.portfolio import PortfolioSchema


class PortfolioDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Portfolio, PortfolioSchema)

    async def add(self, portfolio: PortfolioSchema) -> Optional[PortfolioSchema]:
        lock = asyncio.Lock()
        async with lock:
            return await self._create(portfolio)

    async def delete(self, portfolio_id: int) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(portfolio_id)

    async def get(self, portfolio_id: int) -> Optional[PortfolioSchema]:
        return await self._get(portfolio_id)

    async def update(self, portfolio_id: int, **kwargs) -> Optional[PortfolioSchema]:
        lock = asyncio.Lock()
        async with lock:
            return await self._update(portfolio_id, **kwargs)

    async def list(self, **kwargs) -> Optional[List[PortfolioSchema]]:
        return await self._list(**kwargs)

    async def delete_all(self) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete_all()
