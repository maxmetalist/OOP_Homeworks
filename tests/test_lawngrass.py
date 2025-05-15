import pytest


def test_lawngrass_init(grass1):
    assert grass1.name == "Ну трава..."
    assert grass1.description == "Да, блин, трава и всё"
    assert grass1.price == 1000.0
    assert grass1.quantity == 10
    assert grass1.country == "РФ"
    assert grass1.germination_period == "30 дней"
    assert grass1.color == "Угадай(ответ: зелёная)"


def test_lawngrass_add(grass1, grass2):
    assert grass1 + grass2 == 25000.0


def test_lawngrass_add_error(grass1, smartphone1):
    with pytest.raises(TypeError):
        grass1 + smartphone1
