from datetime import datetime
from typing import List

import pytest

from schemas.operation import OperationSchema


@pytest.fixture
def test_posting_operation() -> OperationSchema:
    return OperationSchema(
        id=1,
        portfolio_id=1,
        value=100,
        created_at=datetime.now()
    )


@pytest.fixture
def test_getting_operation() -> OperationSchema:
    return OperationSchema(
        id=2,
        portfolio_id=1,
        value=-5690340,
        created_at=datetime.now()
    )


@pytest.fixture
def test_deleting_operation() -> OperationSchema:
    return OperationSchema(
        id=3,
        portfolio_id=3,
        value=590,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updating_operation() -> OperationSchema:
    return OperationSchema(
        id=4,
        portfolio_id=1,
        value=0,
        created_at=datetime.now()
    )


@pytest.fixture
def test_updated_operation() -> OperationSchema:
    return OperationSchema(
        id=5,
        portfolio_id=1,
        value=69420,
        created_at=datetime.now()
    )


@pytest.fixture
def test_operation_list() -> List[OperationSchema]:
    return [
        OperationSchema(
            id=i + 6,
            portfolio_id=9,
            value=58,
            created_at=datetime.now()
        )
        for i in range(10)
    ]
