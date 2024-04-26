from django.core.management.base import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        product = Product(name='vin', description='tovar lalala',
        price=4667, quantity=12, added_date='25.05.2002')
        product.save()
        self.stdout.write(f'{product}')