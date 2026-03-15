import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name", ["black bun", "булочка", "bun_123", "bun!@#"])
def test_get_name_returns_name(name):
    bun = Bun(name=name, price=10)
    assert bun.get_name() == name


@pytest.mark.parametrize("price", [0, 1, 999999, 200.5])
def test_get_price_returns_price(price):
    bun = Bun(name="any", price=price)
    assert bun.get_price() == price
