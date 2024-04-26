from django.core.management.base import BaseCommand
from myapp2.models import Client

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
        phone_number="893242", address='secret12', registration_date='25.05.2002')
        client.save()
        self.stdout.write(f'{client}')