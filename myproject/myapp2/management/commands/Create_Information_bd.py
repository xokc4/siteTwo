from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from myapp2.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        client = Client.objects.create(
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Main St',
            registration_date=datetime.now()
        )

        # Создание товаров
        product1 = Product.objects.create(
            name='Product 1',
            description='This is product 1',
            price=19.99,
            quantity=100,
            added_date=datetime.now()
        )

        product2 = Product.objects.create(
            name='Product 2',
            description='This is product 2',
            price=29.99,
            quantity=50,
            added_date=datetime.now()
        )

        # Создание заказов за последние 7, 30 и 365 дней
        orders = [
            Order(client=client, total_amount=product1.price + product2.price,
                  order_date=datetime.now() - timedelta(days=7)),
            Order(client=client, total_amount=product1.price, order_date=datetime.now() - timedelta(days=30)),
            Order(client=client, total_amount=product2.price, order_date=datetime.now() - timedelta(days=365)),
        ]

        # Сохранение заказов в базе данных
        Order.objects.bulk_create(orders)

        # Добавление товаров в заказы
        for order in Order.objects.all():
            order.products.add(product1, product2)