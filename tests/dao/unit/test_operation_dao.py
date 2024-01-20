import pytest

from database import DBCore
from database.dao.OperationDAO import OperationDAO
from database.dao.PortfolioDAO import PortfolioDAO
from settings import TEST


@pytest.mark.asyncio
async def test_operation_deleting(test_deleting_portfolio, test_deleting_operation):
    assert TEST
    session = await DBCore().get_session()
    operation_dao = OperationDAO(session)
    portfolio_dao = PortfolioDAO(session)

    await operation_dao.delete_all()
    await portfolio_dao.delete_all()

    await portfolio_dao.add(test_deleting_portfolio)
    await operation_dao.add(test_deleting_operation)
    portfolio = await portfolio_dao.get(test_deleting_portfolio.id)
    assert portfolio.deposited_money == test_deleting_operation.value

    await operation_dao.delete(test_deleting_operation.id)
    portfolio = await portfolio_dao.get(test_deleting_portfolio.id)
    assert portfolio.deposited_money == 0
    getting_operation = await operation_dao.get(test_deleting_operation.id)
    assert getting_operation is None


@pytest.mark.asyncio
async def test_operation_updating(test_updating_portfolio, test_updating_operation, test_updating_operation2):
    assert TEST
    session = await DBCore().get_session()
    operation_dao = OperationDAO(session)
    portfolio_dao = PortfolioDAO(session)

    await operation_dao.delete_all()
    await portfolio_dao.delete_all()

    new_value = 777
    await portfolio_dao.add(test_updating_portfolio)
    await operation_dao.add(test_updating_operation)
    await operation_dao.add(test_updating_operation2)

    portfolio = await portfolio_dao.get(test_updating_portfolio.id)
    assert portfolio.deposited_money == test_updating_operation.value + test_updating_operation2.value

    updated_operation = await operation_dao.update(test_updating_operation.id, value=new_value)
    portfolio = await portfolio_dao.get(test_updating_portfolio.id)
    assert updated_operation.value == new_value
    assert portfolio.deposited_money == 757


@pytest.mark.asyncio
async def test_operation_list(test_inserting_portfolio, test_list_of_operations):
    assert TEST
    session = await DBCore().get_session()
    operation_dao = OperationDAO(session)
    portfolio_dao = PortfolioDAO(session)
    await portfolio_dao.add(test_inserting_portfolio)
    await operation_dao.delete_all()

    for operation in test_list_of_operations:
        await operation_dao.add(operation)

    operations_portfolio_id = test_list_of_operations[0].portfolio_id

    getting_operations = await operation_dao.list(portfolio_id=operations_portfolio_id)
    assert getting_operations == test_list_of_operations


@pytest.mark.asyncio
async def test_operation_inserting(test_inserting_portfolio, test_inserting_operation):
    assert TEST
    session = await DBCore().get_session()

    operation_dao = OperationDAO(session)
    await operation_dao.delete_all()
    portfolio_dao = PortfolioDAO(session)
    await portfolio_dao.delete_all()

    await portfolio_dao.add(test_inserting_portfolio)
    await operation_dao.add(test_inserting_operation)

    portfolio = await portfolio_dao.get(test_inserting_portfolio.id)
    assert portfolio.deposited_money == test_inserting_operation.value
