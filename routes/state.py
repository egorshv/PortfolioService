from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.StateDAO import StateDAO
from routes.utils import get_async_session
from schemas.state import StateSchema

state_router = APIRouter()


@state_router.get('/state', response_model=Optional[List[StateSchema]])
async def get_states(portfolio_id: int,
                     session: AsyncSession = Depends(get_async_session)) -> Optional[List[StateSchema]]:
    dao = StateDAO(session)
    states = await dao.list(
        portfolio_id=portfolio_id
    )
    return states


@state_router.get('/state/{state_id}', response_model=Optional[StateSchema])
async def get_state(state_id: int, session: AsyncSession = Depends(get_async_session)) -> Optional[StateSchema]:
    dao = StateDAO(session)
    state = await dao.get(state_id)
    return state


@state_router.post('/state', response_model=Optional[StateSchema])
async def post_state(state: StateSchema, session: AsyncSession = Depends(get_async_session)) -> Optional[StateSchema]:
    dao = StateDAO(session)
    created_state = await dao.add(state)
    return created_state


@state_router.delete('/state/{state_id}')
async def delete_state(state_id: int, session: AsyncSession = Depends(get_async_session)):
    dao = StateDAO(session)
    await dao.delete(state_id)
    return {'result': 'state deleted'}


@state_router.put('/state/{state_id}', response_model=Optional[StateSchema])
async def update_state(state_id: int, state: StateSchema,
                       session: AsyncSession = Depends(get_async_session)) -> Optional[StateSchema]:
    dao = StateDAO(session)
    updated_state = await dao.update(state_id, **state.model_dump())
    return updated_state

