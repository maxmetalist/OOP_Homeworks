from src.products import Product


class Smartphone(Product):
    """Класс-наследник от родительского класса Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод сложения экземпляров класса Smartphone(складывается цена, умноженная на количество)"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


# if __name__ == "__main__":
#     smartphone = Smartphone(
#         "Samsung Galaxy C23 Ultra",
#         "256GB," "Серый цвет, 200MP камера",
#         180000.0,
#         1,
#         "2,50 Ghz",
#         "C23 Ultra",
#         "256GB",
#         "Black",
#     )
#
#     print(smartphone.name)
#     print(smartphone.description)
#     print(smartphone.price)
#     print(smartphone.quantity)
#
#     print(smartphone.efficiency)
#     print(smartphone.model)
#     print(smartphone.memory)
#     print(smartphone.color)
#
#     smartphone1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 1, "2,20 Ghz", "Iphone 15", "512GB", "Silver")
#     product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     print(smartphone + smartphone1)
#     print(smartphone + product2)
