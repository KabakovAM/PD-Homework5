from django.shortcuts import render
from . import forms
from Ex007.models import Good
from django.core.files.storage import FileSystemStorage

def good_update(request):
    if request.method == 'POST':
        form = forms.GoodUpdate(request.POST)
        if form.is_valid():
            pk = form.cleaned_data['pk']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            good = Good.objects.filter(pk=pk).first()
            if good is not None:
                good.name = name
                good.description = description
                good.price = price
                good.quantity = quantity
                good.save()
                message = 'Товар изменён'
            else:
                message = 'Проверьте данные товара'
    else:
        form = forms.GoodUpdate()
        message = 'Введите данные'
    return render(request, 'Ex007/good_update.html', {'form': form, 'message': message})

def good_image(request):
    if request.method == 'POST':
        form = forms.GoodImage(request.POST, request.FILES)
        if form.is_valid():
            pk = form.cleaned_data['pk']
            image = form.cleaned_data['image']
            good = Good.objects.filter(pk=pk).first()
            if good is not None:
                good.picture = image
                good.save()
                message = 'Фото добавлено'
            else:
                message = 'Проверьте данные товара'
    else:
        form = forms.GoodImage()
        message = 'Добавьте фото'
    return render(request, 'Ex007/good_image.html', {'form': form, 'message': message})