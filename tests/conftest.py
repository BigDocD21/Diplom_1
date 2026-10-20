import pytest
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
praktikum_path = os.path.join(project_root, '..', 'praktikum')

if praktikum_path not in sys.path:
    sys.path.insert(0, praktikum_path)

@pytest.fixture
def mock_bun():
    from unittest.mock import MagicMock
    fake = MagicMock()
    fake.get_name.return_value = "Mock Bun"
    fake.get_price.return_value = 50.0
    return fake

@pytest.fixture
def mock_ingredient():
    from unittest.mock import MagicMock
    fake = MagicMock()
    fake.get_name.return_value = "Mock Ingredient"
    fake.get_price.return_value = 30.0
    fake.get_type.return_value = "filling"
    return fake