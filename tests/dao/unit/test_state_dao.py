import pytest

from settings import TEST
from database.DBCore import DBCore
from database.dao.StateDAO import StateDAO
from database.models.state import State


@pytest.mark.asyncio
async def test_state_inserting(test_inserting_state):
    assert TEST
    session = await DBCore().get_session()
    dao = StateDAO(session)
    await dao.delete_all()

    await dao.add(test_inserting_state)
    getting_state = await dao.get(test_inserting_state.id)

    assert getting_state == test_inserting_state


@pytest.mark.asyncio
async def test_state_deleting(test_deleting_state):
    assert TEST
    session = await DBCore().get_session()
    dao = StateDAO(session)
    await dao.delete_all()

    await dao.add(test_deleting_state)
    await dao.delete(test_deleting_state.id)
    getting_state = await dao.get(test_deleting_state.id)
    assert getting_state is None


@pytest.mark.asyncio
async def test_state_updating(test_updating_state):
    assert TEST
    session = await DBCore().get_session()
    dao = StateDAO(session)
    await dao.delete_all()

    portfolio_id = 656

    await dao.add(test_updating_state)
    updated_state = await dao.update(test_updating_state.id, portfolio_id=portfolio_id)
    assert updated_state.portfolio_id == portfolio_id


@pytest.mark.asyncio
async def test_state_list(test_list_of_states):
    assert TEST
    session = await DBCore().get_session()
    dao = StateDAO(session)
    await dao.delete_all()

    for state in test_list_of_states:
        await dao.add(state)

    getting_state_list = await dao.list(portfolio_id=2)
    assert getting_state_list == test_list_of_states
