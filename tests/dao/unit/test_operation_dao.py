import pytest

from database import DBCore
from database.dao.OperationDAO import OperationDAO
from settings import TEST


@pytest.mark.asyncio
async def test_operation_inserting(test_inserting_operation):
    assert TEST
    session = await DBCore().get_session()
    dao = OperationDAO(session)
    await dao.delete_all()

    await dao.add(test_inserting_operation)
    getting_operation = await dao.get(test_inserting_operation.id)
    assert test_inserting_operation == getting_operation


@pytest.mark.asyncio
async def test_operation_deleting(test_deleting_operation):
    assert TEST
    session = await DBCore().get_session()
    dao = OperationDAO(session)
    await dao.delete_all()

    await dao.add(test_deleting_operation)
    await dao.delete(test_deleting_operation.id)
    getting_operation = await dao.get(test_deleting_operation.id)
    assert getting_operation is None


@pytest.mark.asyncio
async def test_operation_updating(test_updating_operation):
    assert TEST
    session = await DBCore().get_session()
    dao = OperationDAO(session)
    await dao.delete_all()

    new_value = 777
    await dao.add(test_updating_operation)
    updated_operation = await dao.update(test_updating_operation.id, value=new_value)
    assert updated_operation.value == new_value


@pytest.mark.asyncio
async def test_operation_list(test_list_of_operations):
    assert TEST
    session = await DBCore().get_session()
    dao = OperationDAO(session)
    await dao.delete_all()

    for operation in test_list_of_operations:
        await dao.add(operation)

    operations_portfolio_id = test_list_of_operations[0].portfolio_id

    getting_operations = await dao.list(portfolio_id=operations_portfolio_id)
    assert getting_operations == test_list_of_operations
