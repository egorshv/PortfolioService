import asyncio
from typing import List, Optional

from database.dao.BaseDAO import BaseDAO
from database.MongoClientSingleton import MongoClientSingleton
from schemas.portfolio import Portfolio
from schemas.state import State
from schemas.trade import Trade
from settings import MONGO_DB


class PortfolioDAO(BaseDAO):
    def __init__(self, collection_name: str):
        client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
        super().__init__(client, collection_name, Portfolio)

    async def add(self, portfolio: Portfolio) -> None:
        portfolios = await self._list()
        portfolio_names = [portfolio.name for portfolio in portfolios]
        if portfolio.name not in portfolio_names:
            lock = asyncio.Lock()
            async with lock:
                await self._add(portfolio)

    async def add_trade(self, trade: Trade, portfolio_name: str, user_id: int) -> None:
        portfolio: Portfolio = await self.get(portfolio_name, user_id)
        trades: List[Trade] = portfolio.trades + [trade]
        await self.update(portfolio_name, user_id, trades=trades)

    async def add_state(self, state: State, portfolio_name: str, user_id: int):
        portfolio: Portfolio = await self.get(portfolio_name, user_id)
        states: List[State] = portfolio.states + [state]
        await self.update(portfolio_name, user_id, states=states)

    async def delete(self, portfolio_name: str, user_id: int) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(name=portfolio_name, user_id=user_id)

    async def get(self, portfolio_name: str, user_id: int) -> Optional[Portfolio]:
        return await self._get(name=portfolio_name, user_id=user_id)

    async def update(self, portfolio_name: str, user_id: int, **kwargs) -> Optional[Portfolio]:
        filtered_params = {key: value for key, value in kwargs.items() if value is not None}
        lock = asyncio.Lock()
        async with lock:
            return await self._update({'name': portfolio_name, 'user_id': user_id}, **filtered_params)

    async def list(self, **kwargs) -> Optional[List[Portfolio]]:
        filtered_params = {key: value for key, value in kwargs.items() if value is not None}
        return await self._list(**filtered_params)

    async def delete_many(self, **kwargs):
        filtered_params = {key: value for key, value in kwargs.items() if value is not None}
        await self._delete_many(**filtered_params)
