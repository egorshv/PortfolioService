import pytest
from fastapi.encoders import jsonable_encoder

from settings import TEST
from tests.routes.utils import clear_state_db


@pytest.mark.asyncio
async def test_state_posting(test_client, test_posting_state):
    assert TEST
    await clear_state_db()

    response = test_client.post('/state', json=jsonable_encoder(test_posting_state))
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_posting_state)


@pytest.mark.asyncio
async def test_state_getting(test_client, test_getting_state):
    assert TEST
    await clear_state_db()

    response = test_client.post('/state', json=jsonable_encoder(test_getting_state))
    assert response.status_code == 200

    response = test_client.get(f'/state/{test_getting_state.id}')
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_getting_state)


@pytest.mark.asyncio
async def test_state_deleting(test_client, test_deleting_state):
    assert TEST
    await clear_state_db()

    response = test_client.post('/state', json=jsonable_encoder(test_deleting_state))
    assert response.status_code == 200

    response = test_client.delete(f'/state/{test_deleting_state.id}')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_state_updating(test_client, test_updating_state,
                              test_updated_state):
    assert TEST
    await clear_state_db()

    response = test_client.post('/state', json=jsonable_encoder(test_updating_state))
    assert response.status_code == 200

    response = test_client.put(f'/state/{test_updating_state.id}', json=jsonable_encoder(test_updated_state))
    assert response.json() == jsonable_encoder(test_updated_state)


@pytest.mark.asyncio
async def test_state_list(test_client, test_states_list):
    assert TEST
    await clear_state_db()

    for state in test_states_list:
        response = test_client.post('/state', json=jsonable_encoder(state))
        assert response.status_code == 200

    response = test_client.get(f'/state?portfolio_id={test_states_list[0].portfolio_id}')
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_states_list)
