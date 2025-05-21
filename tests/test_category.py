import pytest

from src.products import Product


def test_category_init(product1_, product2_):
    """тест инициализации экземпляра класса Category"""
    assert product1_.name == "Смартфон"
    assert product1_.description == "Huawey Honor 10"
    assert len(product1_.products_list) == 3
    assert product2_.name == "Смартфон"
    assert product2_.description == "Xiaomy Redmy 12"
    assert len(product2_.products_list) == 2
    assert product1_.category_count == 2
    assert product2_.category_count == 2
    assert product1_.product_count == 5
    assert product2_.product_count == 5


def test_products_property(product1_):
    """тест геттера для приватного атрибута products"""
    assert product1_.products == (
        "Смартфон, 20000.0, Остаток: 10 шт.\n"
        "Телевизор, 50000.0, Остаток: 10 шт.\n"
        "Смартфон, 20000.0, Остаток: 10 шт.\n"
    )


def test_products_setter(product1_, product):
    """тест сеттера для приватного атрибута products"""
    assert len(product1_.products_list) == 3
    product1_.products = product
    assert len(product1_.products_list) == 4


def test_category_str(product):
    """тест преобразование экземпляра в строку"""
    assert str(product) == "Игровая консоль, 100000.0, Остаток: 10 шт."


def test_products_setter_error(product1_):
    """тест сеттера на ошибку(когда пытаемся добавить что-то не класса Product"""
    with pytest.raises(TypeError):
        product1_.products = 1


def test_products_setter_normal(product1_, smartphone1):
    """тест сеттера на нормальную работу"""
    assert product1_.products == (
        "Смартфон, 20000.0, Остаток: 10 шт.\n"
        "Телевизор, 50000.0, Остаток: 10 шт.\n"
        "Смартфон, 20000.0, Остаток: 10 шт.\n"
    )


def test_middle_price(product1_, product_no_quantity):
    """тест на работу метода вычисления средней цены товара в категории(при нулевом и не нулевом количестве)"""
    assert product1_.middle_price() == 30000.0
    assert product_no_quantity.middle_price() == 0


def test_custom_exception(capsys, product1_):
    """тест перехвата выводных сообщений кастомной ошибки(на нулевое и не нулевое количество)"""
    assert len(product1_.products_list) == 3

    product_add = Product("Смартфон", "Huawey Nova 10", 20000.00, 0)
    product1_.products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == (
        "Круто, конечно, но у тебя количество ноль." "Как мы добавим дырку от бублика?"
    )
    assert message.out.strip().split("\n")[-1] == "Обработка завершена. Как то так..."

    product_add = Product("Смартфон", "Huawey Nova 10", 20000.00, 10)
    product1_.products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Ладно, так и быть. Товар добавлен."
    assert message.out.strip().split("\n")[-1] == "Обработка завершена. Как то так..."
