from datetime import datetime
from typing import List

import pytest

from schemas.currency import Currency
from schemas.state import StateSchema


@pytest.fixture
def test_portfolio_states() -> List[StateSchema]:
    return [
        StateSchema(
            id=i + 1,
            portfolio_id=1,
            usd_result=15 + i,
            rub_result=22 + i * 3 - 12,
            created_at=datetime.now()
        )
        for i in range(20)
    ]


@pytest.fixture
def test_currency() -> Currency:
    return Currency.RUB


@pytest.fixture
def test_empty_portfolio_states() -> List[StateSchema]:
    return []
