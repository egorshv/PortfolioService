from datetime import datetime
from typing import List

import pytest

from schemas.state import StateSchema


@pytest.fixture
def test_inserting_state() -> StateSchema:
    return StateSchema(
        id=1,
        portfolio_id=1,
        usd_result=14,
        rub_result=25,
        created_at=datetime.now()
    )


@pytest.fixture
def test_deleting_state() -> StateSchema:
    return StateSchema(
        id=2,
        portfolio_id=1,
        usd_result=0,
        rub_result=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updating_state() -> StateSchema:
    return StateSchema(
        id=3,
        portfolio_id=1,
        usd_result=10,
        rub_result=20,
        created_at=datetime.now()
    )


@pytest.fixture
def test_list_of_states() -> List[StateSchema]:
    return [
        StateSchema(
            id=i + 4,
            portfolio_id=2,
            usd_result=i * 4,
            rub_result=i * 6,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
