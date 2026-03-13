from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture()
def burger():
    return Burger()


def test_set_buns_sets_bun_reference(burger):
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient_appends_to_list(burger):
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient_deletes_by_index(burger):
    ing1, ing2, ing3 = Mock(), Mock(), Mock()
    burger.ingredients = [ing1, ing2, ing3]

    burger.remove_ingredient(1)

    assert burger.ingredients == [ing1, ing3]


@pytest.mark.parametrize(
    "start_order, index, new_index, expected_order",
    [
        (["a", "b", "c"], 0, 2, ["b", "c", "a"]),
        (["a", "b", "c"], 2, 0, ["c", "a", "b"]),
        (["a", "b", "c", "d"], 1, 1, ["a", "b", "c", "d"]),
    ],
)
def test_move_ingredient_changes_order(burger, start_order, index, new_index, expected_order):
    # Use simple sentinel objects to check ordering exactly
    ingredients = [object() for _ in start_order]
    burger.ingredients = ingredients.copy()

    # Map expected order by indices in start_order
    # (We only care about relative moves, not values)
    burger.move_ingredient(index, new_index)

    # Compare by object identity ordering
    expected = ingredients.copy()
    expected.insert(new_index, expected.pop(index))

    assert burger.ingredients == expected


@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected_total",
    [
        (100, [], 200),
        (50.5, [10, 20], 101.0 + 30),
        (0, [1, 2, 3], 6),
    ],
)
def test_get_price_uses_bun_twice_and_sums_ingredients(
    burger, bun_price, ingredient_prices, expected_total
):
    bun = Mock()
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)

    for p in ingredient_prices:
        ing = Mock()
        ing.get_price.return_value = p
        burger.add_ingredient(ing)

    assert burger.get_price() == expected_total


def test_get_receipt_builds_expected_text(burger):
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    burger.set_buns(bun)

    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100

    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 100

    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt()

    expected = "\n".join(
        [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)\n",
            "Price: 400",
        ]
    )

    assert receipt == expected
