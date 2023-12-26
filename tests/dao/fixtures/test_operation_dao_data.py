from datetime import datetime
from typing import List

import pytest
from schemas.operation import OperationSchema


@pytest.fixture
def test_inserting_operation() -> OperationSchema:
    return OperationSchema(
        id=1,
        portfolio_id=1,
        value=-100,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updating_operation() -> OperationSchema:
    return OperationSchema(
        id=2,
        portfolio_id=1,
        value=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_deleting_operation() -> OperationSchema:
    return OperationSchema(
        id=3,
        portfolio_id=3,
        value=1,
        created_at=datetime.now()
    )


@pytest.fixture
def test_list_of_operations() -> List[OperationSchema]:
    return [
        OperationSchema(
            id=i + 4,
            portfolio_id=1,
            value=i * 100,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
