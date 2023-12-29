from datetime import datetime
from typing import List

import pytest

from schemas.state import StateSchema


@pytest.fixture
def test_posting_state() -> StateSchema:
    return StateSchema(
        id=1,
        portfolio_id=1,
        usd_result=0,
        rub_result=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_getting_state() -> StateSchema:
    return StateSchema(
        id=2,
        portfolio_id=1,
        usd_result=0,
        rub_result=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_deleting_state() -> StateSchema:
    return StateSchema(
        id=3,
        portfolio_id=1,
        usd_result=0,
        rub_result=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updating_state() -> StateSchema:
    return StateSchema(
        id=4,
        portfolio_id=1,
        usd_result=0,
        rub_result=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updated_state() -> StateSchema:
    return StateSchema(
        id=5,
        portfolio_id=2,
        usd_result=500,
        rub_result=100500,
        created_at=datetime.now()
    )


@pytest.fixture
def test_states_list() -> List[StateSchema]:
    return [
        StateSchema(
            id=i + 5,
            portfolio_id=7,
            usd_result=500,
            rub_result=100500,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
