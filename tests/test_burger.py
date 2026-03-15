from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_set_buns_sets_bun_reference(burger: Burger, mock_bun: Mock):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient_adds_to_list(burger: Burger, mock_ingredient: Mock):
    burger.add_ingredient(mock_ingredient)
    assert burger.ingredients == [mock_ingredient]


def test_remove_ingredient_removes_by_index(burger: Burger, mock_ingredient: Mock):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert burger.ingredients == []


def test_move_ingredient_swaps_positions(burger: Burger):
    ing1 = Mock(spec=Ingredient)
    ing2 = Mock(spec=Ingredient)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ing2, ing1]


def test_get_price_returns_total(burger: Burger):
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 10

    ing1 = Mock(spec=Ingredient)
    ing1.get_price.return_value = 5
    ing2 = Mock(spec=Ingredient)
    ing2.get_price.return_value = 7

    burger.set_buns(bun)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert burger.get_price() == 10 * 2 + 5 + 7


def test_get_receipt_contains_names_and_total(burger: Burger):
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "B"
    bun.get_price.return_value = 10

    ing = Mock(spec=Ingredient)
    ing.get_name.return_value = "I"
    ing.get_price.return_value = 5

    burger.set_buns(bun)
    burger.add_ingredient(ing)

    receipt = burger.get_receipt()

    assert "B" in receipt
    assert "I" in receipt
    assert str(burger.get_price()) in receipt
