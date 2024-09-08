# tests/test_crud.py

from unittest.mock import MagicMock
import pytest
from app.crud.investor import get_investors, get_investors_by_id, get_commitments_by_investor_id
from app.models import Investor, Commitment

@pytest.fixture
def mock_db():
    db = MagicMock()
    return db

def test_get_investors(mock_db):
    # Setup mock return values
    mock_db.query().offset().limit().all.return_value = [
        Investor(id=1, investor_name="Investor A"),
        Investor(id=2, investor_name="Investor B"),
    ]
    # Call function
    result = get_investors(mock_db, skip=0, limit=10)
    # Assertions
    assert len(result) == 2
    assert result[0].investor_name == "Investor A"

def test_get_investors_by_id(mock_db):
    # Setup mock return values
    mock_db.query().filter().first.return_value = Investor(id=1, investor_name="Investor A")
    mock_db.query().filter().scalar.return_value = 1000
    # Call function
    result = get_investors_by_id(mock_db, 1)
    # Assertions
    assert result.id == 1
    assert result.investor_name == "Investor A"

def test_get_commitments_by_investor_id(mock_db):
    # Setup mock return values
    mock_db.query().filter().all.return_value = [
        Commitment(id=1, asset_class="Class A", amount=100),
        Commitment(id=2, asset_class="Class B", amount=200),
    ]
    # Call function
    result = get_commitments_by_investor_id(mock_db, 1)
    # Assertions
    assert len(result) == 2
    assert result[0].asset_class == "Class A"
