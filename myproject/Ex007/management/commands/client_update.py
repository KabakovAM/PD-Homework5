from django.core.management.base import BaseCommand
from Ex007.models import Client

class Command(BaseCommand):
    help = 'Read client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('phone', type=str, help='Client phone')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).filter()
        if client is not None:
            client.phone = phone        
        self.stdout.write(f'{client}')