from src.products import Product


def test_products_init(product):
    """тест на инициализацию экземпляра класса Product"""
    assert product.name == "Игровая консоль"
    assert product.description == "Sony Playstation 5"
    assert product.price == 100000
    assert product.quantity == 10


def test_product_add_init():
    """тест на инициализацию добавления продукта"""
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product_zero_price(capsys, product):
    """тест на выводное сообщение при нулевой цене"""
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product_low_price(capsys, product):
    """тест на выводное сообщение при нулевой цене"""
    product.price = 10000.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена понизилась? Да ладно!!! А чё так можно было?!!"


def test_new_product_new_price(product):
    """тест на изменение цены(когда цена уменьшилась результат не должен измениться"""
    product.price = 10000.0
    assert product.price == 100000.0


def test_product_str(product):
    """тест на строковое значение класса Product"""
    assert str(product) == "Игровая консоль, 100000.0, Остаток: 10 шт."


def test_add_products(product_1, product_2):
    """тест на сложение экземпляров класса Product"""
    assert product_1 + product_2 == 400000.00
