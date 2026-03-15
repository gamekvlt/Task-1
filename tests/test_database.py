from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_available_buns_returns_list_of_buns(database: Database):
    buns = database.available_buns()

    assert isinstance(buns, list)
    assert len(buns) > 0
    assert all(isinstance(b, Bun) for b in buns)


def test_available_ingredients_returns_list_of_ingredients(database: Database):
    ingredients = database.available_ingredients()

    assert isinstance(ingredients, list)
    assert len(ingredients) > 0
    assert all(isinstance(i, Ingredient) for i in ingredients)


def test_available_buns_returns_new_list_each_call(database: Database):
    first = database.available_buns()
    second = database.available_buns()

    assert first is not second


def test_available_ingredients_returns_new_list_each_call(database: Database):
    first = database.available_ingredients()
    second = database.available_ingredients()

    assert first is not second
