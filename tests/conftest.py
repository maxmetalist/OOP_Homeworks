import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product1_():
    return Category(
        name="Смартфон",
        description="Huawey Honor 10",
        products=[
            Product("Смартфон", "Huawey Honor 10", 20000.00, 10),
            Product("Телевизор", "Sony Bravia", 50000.00, 10),
            Product("Смартфон", "Xiaomy Redmy 12", 20000, 10),
        ],
    )


@pytest.fixture
def product2_():
    return Category(
        name="Смартфон",
        description="Xiaomy Redmy 12",
        products=[
            Product("Смартфон", "Huawey Nova 10", 20000.00, 10),
            Product("Телевизор", "Samsung Qled", 50000.00, 10),
        ],
    )


@pytest.fixture
def product():
    return Product("Игровая консоль", "Sony Playstation 5", 100000, 10)
