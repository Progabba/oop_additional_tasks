class Product:
    """
    Класс для описания товара в магазине
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.product = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]
categories = []
for category in data:
    products = []
    for product in category['products']:
        print(product)
        products.append(Product(**product))
    category['products'] = products
    categories.append(Category(**category))

# """"""
# Ожидаемый ответ:
#
# {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}
# {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}
# {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}
# {'name': '55 QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantit
# """