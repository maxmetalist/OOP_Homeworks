from src.products import Product


class LawnGrass(Product):
    """класс-наследник от родительского класса Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод сложения экземпляров класса LawnGrass(складывается цена, умноженная на количество)"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


# if __name__ == "__main__":
#     grass = LawnGrass("Ну трава...", "Да, блин, трава и всё", 1000.0, 10, "РФ", "30 дней", "Угадай(ответ: зелёная)")
#     print(grass.name)
#     print(grass.description)
#     print(grass.price)
#     print(grass.quantity)
#
#     print(grass.country)
#     print(grass.germination_period)
#     print(grass.color)
#
#     grass1 = LawnGrass(
#         "Да, тоже трава",
#         "Трава, как её ещё обозвать",
#         1500.0,
#         10,
#         "Ну пусть GBR",
#         "30 дней",
#         "Прикинь, чёрная(селекция!!!)",
#     )
#     print(grass + grass1)
