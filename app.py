from fastapi import FastAPI

from routes.operation import operation_router
from routes.portfolio import portfolio_router
from routes.state import state_router
from routes.trade import trade_router

app = FastAPI()

app.include_router(portfolio_router)
app.include_router(state_router)
app.include_router(operation_router)
app.include_router(trade_router)
