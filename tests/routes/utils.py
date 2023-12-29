from database import DBCore
from database.dao.OperationDAO import OperationDAO
from database.dao.PortfolioDAO import PortfolioDAO
from database.dao.StateDAO import StateDAO
from database.dao.TradeDAO import TradeDAO


async def clear_portfolio_db():
    session = await DBCore().get_session()
    dao = PortfolioDAO(session)
    await dao.delete_all()


async def clear_trade_db():
    session = await DBCore().get_session()
    dao = TradeDAO(session)
    await dao.delete_all()


async def clear_state_db():
    session = await DBCore().get_session()
    dao = StateDAO(session)
    await dao.delete_all()


async def clear_operation_db():
    session = await DBCore().get_session()
    dao = OperationDAO(session)
    await dao.delete_all()
