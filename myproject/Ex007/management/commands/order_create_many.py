from django.core.management.base import BaseCommand
from Ex007.models import Order, Client, Good

class Command(BaseCommand):
    help = 'Create Order'
  
    def handle (self, *args, **kwargs):
        for i in range(1,11):
            order = Order(client = Client.objects.get(pk=i))
            order.save()
            price = 0
            for k in range(5):
                good = Good.objects.get(pk=k+4)
                order.good.add(good.pk)
                price += good.price
            order.total = price
            order.save()
            self.stdout.write(f'{order}')

