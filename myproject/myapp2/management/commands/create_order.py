from django.core.management.base import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = "Create user."
def handle(self, *args, **kwargs):
    product = Product(client=1, products=1,
    total_amount=4667,  order_date='25.05.2002')
    product.save()
    self.stdout.write(f'{product}')