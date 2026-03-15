import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_get_type_returns_type(ingredient_type):
    ingredient = Ingredient(ingredient_type=ingredient_type, name="any", price=10)
    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize("name", ["hot sauce", "соус", "name_123", "name!@#"])
def test_get_name_returns_name(name):
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=name, price=10)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("price", [0, 1, 250.25, 999999])
def test_get_price_returns_price(price):
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="any", price=price)
    assert ingredient.get_price() == price
