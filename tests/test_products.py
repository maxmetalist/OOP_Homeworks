def test_products_init(product):
    assert product.name == "Игровая консоль"
    assert product.description == "Sony Playstation 5"
    assert product.price == 100000
    assert product.quantity == 10
