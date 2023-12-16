from django.core.management.base import BaseCommand
from Ex007.models import Client

class Command(BaseCommand):
    help = 'Create client'
  
    def handle (self, *args, **kwargs):
        for i in range(10):
            client = Client(name=f'Client{i}', email = f'email{i}@example.com', phone = f'phone{i}', adress = f'adress{i}')
            client.save()
            self.stdout.write(f'{client}')