from django import forms

class GoodUpdate(forms.Form):
    pk = forms.IntegerField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()

class GoodImage(forms.Form):
    pk = forms.IntegerField()
    image = forms.ImageField()