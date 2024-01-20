import asyncio
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.BaseDAO import BaseDAO
from database.dao.PortfolioDAO import PortfolioDAO
from database.models.operation import Operation
from schemas.operation import OperationSchema


class OperationDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Operation, OperationSchema)
        self.portfolio_dao = PortfolioDAO(session)

    async def add(self, operation: OperationSchema) -> Optional[OperationSchema]:
        portfolio = await self.portfolio_dao.get(operation.portfolio_id)

        await self.portfolio_dao.update(
            portfolio_id=operation.portfolio_id,
            deposited_money=portfolio.deposited_money + operation.value
        )

        lock = asyncio.Lock()
        async with lock:
            return await self._create(operation)

    async def delete(self, operation_id: int) -> None:
        operation = await self.get(operation_id)
        portfolio = await self.portfolio_dao.get(operation.portfolio_id)

        await self.portfolio_dao.update(
            portfolio_id=portfolio.id,
            deposited_money=portfolio.deposited_money - operation.value
        )

        lock = asyncio.Lock()
        async with lock:
            await self._delete(operation_id)

    async def get(self, operation_id: int) -> Optional[OperationSchema]:
        return await self._get(operation_id)

    async def update(self, operation_id: int, **kwargs) -> Optional[OperationSchema]:
        if kwargs.get('value') is not None:
            operation = await self.get(operation_id)
            portfolio = await self.portfolio_dao.get(operation.portfolio_id)
            diff_value = kwargs.get('value') - operation.value
            await self.portfolio_dao.update(
                portfolio_id=portfolio.id,
                deposited_money=portfolio.deposited_money + diff_value
            )

        lock = asyncio.Lock()
        async with lock:
            return await self._update(operation_id, **kwargs)

    async def list(self, **kwargs) -> Optional[List[OperationSchema]]:
        return await self._list(**kwargs)

    async def delete_all(self) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete_all()
