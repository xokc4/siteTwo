from datetime import datetime, timedelta
import random
from django.core.management.base import BaseCommand
from myapp2.models import Client, Product, Order

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
# Получение клиента по ID
        client = Client.objects.get(id=3)

# Создание товаров
        products = [
    Product.objects.create(name=f'Product {i}', description=f'This is product {i}', price=19.99, quantity=100, added_date=datetime.now() - timedelta(days=i)) for i in range(1, 4)
]

# Создание заказов за последние 7 дней с разными товарами
        for i in range(7, 0, -1):

            random_days = 29 - random.randint(1, 7)  # Генерация случайного числа от 1 до 7
            order_date = str(random_days)+"-04-2024"
            order = Order.objects.create(client=client, total_amount=products[0].price, order_date=order_date)
            order.products.add(products[0])

# Создание заказов за последние 30 дней с разными товарами
        for i in range(30, 27, -1):
            random_days = random.randint(1, 30)  # Генерация случайного числа от 1 до 30
            order_date = datetime.now() - timedelta(days=random_days)
            order = Order.objects.create(client=client, total_amount=products[1].price, order_date=order_date)
            order.products.add(products[1])

# Создание заказов за последний год с разными товарами
        for i in range(365, 362, -1):
            random_days = random.randint(1, 365)  # Генерация случайного числа от 1 до 365
            order_date = datetime.now() - timedelta(days=random_days)
            order = Order.objects.create(client=client, total_amount=products[2].price, order_date=order_date)
            order.products.add(products[2])