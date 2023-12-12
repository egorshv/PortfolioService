TEST = True

if TEST:
    MONGO_DB = {
        'NAME': 'invest_stats',
        'COLLECTION': 'test_portfolio',
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'PASSWORD': ''
    }
else:
    MONGO_DB = {
        'NAME': 'invest_stats',
        'COLLECTION': 'portfolio',
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'PASSWORD': ''
    }
