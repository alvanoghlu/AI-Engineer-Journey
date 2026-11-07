import pytest

from product import Product, most_expensive


def test_total_value():
    product = Product("Laptop", 1200.0, 2)

    assert product.total_value() == 2400.0


def test_most_expensive():
    products = [
        Product("Laptop", 1200.0, 2),
        Product("Mouse", 25.0, 3),
        Product("Keyboard", 60.0, 2),
    ]

    result = most_expensive(products)

    assert result.name == "Laptop"


def test_empty_products():
    products = []

    with pytest.raises(ValueError):
        most_expensive(products)
