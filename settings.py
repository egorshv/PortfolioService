TEST = True

if TEST:
    MONGO_DB = {
        'NAME': 'invest_stats',
        'PORTFOLIO_COLLECTION': 'test_portfolio',
        'STATE_COLLECTION': 'test_state',
        'OPERATION_COLLECTION': 'test_operation',
        'TRADE_COLLECTION': 'test_trade',
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'PASSWORD': ''
    }
else:
    MONGO_DB = {
        'NAME': 'invest_stats',
        'PORTFOLIO_COLLECTION': 'portfolio',
        'STATE_COLLECTION': 'state',
        'OPERATION_COLLECTION': 'operation',
        'TRADE_COLLECTION': 'trade',
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'PASSWORD': ''
    }
