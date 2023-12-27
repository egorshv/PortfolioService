from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.OperationDAO import OperationDAO
from routes.utils import get_async_session
from schemas.operation import OperationSchema

operation_router = APIRouter()


@operation_router.get('/operation', response_model=List[OperationSchema])
async def get_operations(portfolio_id: int = None, value: float = None,
                         session: AsyncSession = Depends(get_async_session)) -> List[OperationSchema]:
    dao = OperationDAO(session)
    operations = await dao.list(
        portfolio_id=portfolio_id,
        value=value
    )
    return operations


@operation_router.get('/operation/{operation_id}', response_model=Optional[OperationSchema])
async def get_operation(operation_id: int,
                        session: AsyncSession = Depends(get_async_session)) -> Optional[OperationSchema]:
    dao = OperationDAO(session)
    return await dao.get(operation_id)


@operation_router.post('/operation', response_model=Optional[OperationSchema])
async def post_operation(operation: OperationSchema,
                         session: AsyncSession = Depends(get_async_session)) -> Optional[OperationSchema]:
    dao = OperationDAO(session)
    created_operation = await dao.add(operation)
    return created_operation


@operation_router.put('/operation/{operation_id}', response_model=Optional[OperationSchema])
async def update_operation(operation_id: int, operation: OperationSchema,
                           session: AsyncSession = Depends(get_async_session)) -> Optional[OperationSchema]:
    dao = OperationDAO(session)
    updated_operation = await dao.update(operation_id, **operation.model_dump())
    return updated_operation


@operation_router.delete('/operation/{operation_id}')
async def delete_operation(operation_id: int,
                           session: AsyncSession = Depends(get_async_session)):
    dao = OperationDAO(session)
    await dao.delete(operation_id)
    return {'result': 'operation deleted'}


