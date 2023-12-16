from django.core.management.base import BaseCommand
from Ex007.models import Good

class Command(BaseCommand):
    help = 'Create good'
  
    def handle (self, *args, **kwargs):
        for i in range(100):
            good = Good(name=f'Good{i}', description = f'Description{i}', price = i+100, quantity  = i+50)
            good.save()
            self.stdout.write(f'{good}')