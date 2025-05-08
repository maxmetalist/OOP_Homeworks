def test_category_init(product1_, product2_):
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
    assert product1_.products == (
        "Смартфон, 20000.0. Остаток: 10 шт.\n"
        "Телевизор, 50000.0. Остаток: 10 шт.\n"
        "Смартфон, 20000. Остаток: 10 шт.\n"
    )


def test_products_setter(product1_, product):
    assert len(product1_.products_list) == 3
    product1_.products = product
    assert len(product1_.products_list) == 4
