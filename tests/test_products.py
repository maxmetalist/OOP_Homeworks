from src.products import Product


def test_products_init(product):
    assert product.name == "Игровая консоль"
    assert product.description == "Sony Playstation 5"
    assert product.price == 100000
    assert product.quantity == 10


def test_product_add_init():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product_zero_price(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product_new_price(product):
    product.price = 100000.0
    assert product.price == 100000.0
