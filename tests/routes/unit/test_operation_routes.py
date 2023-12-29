import pytest
from fastapi.encoders import jsonable_encoder

from settings import TEST
from tests.routes.utils import clear_operation_db


@pytest.mark.asyncio
async def test_operation_posting(test_client, test_posting_operation):
    assert TEST
    await clear_operation_db()

    response = test_client.post('/operation', json=jsonable_encoder(test_posting_operation))
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_posting_operation)


@pytest.mark.asyncio
async def test_operation_getting(test_client, test_getting_operation):
    assert TEST
    await clear_operation_db()

    response = test_client.post('/operation', json=jsonable_encoder(test_getting_operation))
    assert response.status_code == 200

    response = test_client.get(f'/operation/{test_getting_operation.id}')
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_getting_operation)


@pytest.mark.asyncio
async def test_operation_deleting(test_client, test_deleting_operation):
    assert TEST
    await clear_operation_db()

    response = test_client.post('/operation', json=jsonable_encoder(test_deleting_operation))
    assert response.status_code == 200

    response = test_client.delete(f'/operation/{test_deleting_operation.id}')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_operation_updating(test_client, test_updating_operation, test_updated_operation):
    assert TEST
    await clear_operation_db()

    response = test_client.post('/operation', json=jsonable_encoder(test_updating_operation))
    assert response.status_code == 200

    response = test_client.put(f'/operation/{test_updating_operation.id}', json=jsonable_encoder(test_updated_operation))
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_updated_operation)


@pytest.mark.asyncio
async def test_get_operation_list(test_client, test_operation_list):
    assert TEST
    await clear_operation_db()

    for operation in test_operation_list:
        response = test_client.post('/operation', json=jsonable_encoder(operation))
        assert response.status_code == 200

    response = test_client.get(f'/operation?portfolio_id={test_operation_list[0].portfolio_id}')
    assert response.status_code == 200
    assert response.json() == jsonable_encoder(test_operation_list)
