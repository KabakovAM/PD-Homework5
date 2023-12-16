from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=200)
    reg_data = models.DateField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, data: {self.reg_data}'

class Good(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    reg_data = models.DateField(auto_now=True)
    picture = models.ImageField(default=None)

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, data: {self.reg_data}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    good = models.ManyToManyField(Good, default=None)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reg_data = models.DateField(auto_now=True)

    def __str__(self):
        return f'Client: {self.client}, total: {self.total}, data: {self.reg_data}'
