import json
import os.path

from src.category import Category
from src.products import Product


def read_json_products(products_path):
    """Функция чтения файла json"""
    abs_path = os.path.abspath(products_path)
    with open(
        abs_path,
        "r",
        encoding="UTF-8",
    ) as file:
        products = json.load(file)
        return products


if __name__ == "__main__":
    products_list = read_json_products("../data/products.json")
    print(products_list)


def products_json(products):
    """Функция преобразования списка из json-файла в объекты соответствующих классов"""
    category = []
    for items in products:
        product = []
        for item in items["products"]:
            product.append(Product(**item))
        items["products"] = product
        category.append(Category(**items))
    return category


if __name__ == "__main__":
    products_list = read_json_products("../data/products.json")
    categorys = products_json(products_list)
    print(categorys)
    print(categorys[0].name)
    print(categorys[0].description)
    print(categorys[0].products[0])
