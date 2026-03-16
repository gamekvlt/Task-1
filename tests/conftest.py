import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient():
    ing = Mock(spec=Ingredient)
    ing.get_name.return_value = "test ingredient"
    ing.get_price.return_value = 50
    return ing


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def sauce_type():
    return INGREDIENT_TYPE_SAUCE


@pytest.fixture
def filling_type():
    return INGREDIENT_TYPE_FILLING
