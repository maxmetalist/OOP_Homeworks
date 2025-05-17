class PrintMixin:
    """класс миксин для вывода сообщений о продукте"""

    def __init__(self):
        """метод инициализации"""
        print(repr(self))

    def __repr__(self):
        """метод переопределения(вывод сообщения в консоль с указанием класса и общих свойств)"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
