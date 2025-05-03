def test_category_init(product1_, product2_):
    assert product1_.name == "Смартфон"
    assert product1_.description == "Huawey Honor 10"
    assert len(product1_.products) == 3
    assert product2_.name == "Смартфон"
    assert product2_.description == "Xiaomy Redmy 12"
    assert len(product2_.products) == 2
    assert product1_.category_count == 2
    assert product2_.category_count == 2
    assert product1_.product_count == 5
    assert product2_.product_count == 5
