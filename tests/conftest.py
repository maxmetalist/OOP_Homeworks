import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product_iterator import ProductIterator
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1_():
    return Category(
        name="Смартфон",
        description="Huawey Honor 10",
        products=[
            Product("Смартфон", "Huawey Honor 10", 20000.00, 10),
            Product("Телевизор", "Sony Bravia", 50000.00, 10),
            Product("Смартфон", "Xiaomy Redmy 12", 20000.00, 10),
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
    return Product("Игровая консоль", "Sony Playstation 5", 100000.00, 10)


@pytest.fixture
def product_iterator(product2_):
    return ProductIterator(product2_)


@pytest.fixture
def product_1():
    return Product("Смартфон", "Huawey Honor 10", 20000.00, 10)


@pytest.fixture
def product_2():
    return Product("Смартфон", "Xiaomy Redmy 12", 20000.00, 10)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy C23 Ultra",
        "256GB,Серый цвет, 200MP камера",
        180000.0,
        1,
        "2,50 Ghz",
        "C23 Ultra",
        "256GB",
        "Black",
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 1, "2,20 Ghz", "Iphone 15", "512GB", "Silver")


@pytest.fixture
def grass1():
    return LawnGrass("Ну трава...", "Да, блин, трава и всё", 1000.0, 10, "РФ", "30 дней", "Угадай(ответ: зелёная)")


@pytest.fixture
def grass2():
    return LawnGrass(
        "Да, тоже трава",
        "Трава, как её ещё обозвать",
        1500.0,
        10,
        "Ну пусть GBR",
        "30 дней",
        "Прикинь, чёрная(селекция!!!)",
    )


@pytest.fixture
def product_no_quantity():
    return Category(name="Смартфон", description="Huawey Honor 10")
