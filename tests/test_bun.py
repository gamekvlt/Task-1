import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0),
    ],
)
def test_bun_getters_return_init_values(name, price):
    bun = Bun(name=name, price=price)

    assert bun.get_name() == name
    assert bun.get_price() == price
