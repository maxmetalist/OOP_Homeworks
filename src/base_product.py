from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """введение базового абстрактного класса"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """метод для добавки продукта(переопределяется в модуле products)"""
        pass
