from django.core.management.base import BaseCommand
from Ex007.models import Client

class Command(BaseCommand):
    help = 'Read client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).filter()
        self.stdout.write(f'{client}')