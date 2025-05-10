import pytest


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.start == 0
    assert next(product_iterator).name == "Смартфон"
    assert next(product_iterator).name == "Телевизор"
    with pytest.raises(StopIteration):
        next(product_iterator)
