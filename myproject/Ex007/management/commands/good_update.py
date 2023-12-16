from django.core.management.base import BaseCommand
from Ex007.models import Good
import decimal

class Command(BaseCommand):
    help = 'Read good by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Good ID')
        parser.add_argument('price', type=decimal, help='Good price')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        good = Good.objects.filter(pk=pk).filter()
        if good is not None:
            good.price = price        
        self.stdout.write(f'{good}')