from django.urls import path
from . import views

urlpatterns = [
    path('good_update/', views.good_update, name='good_update'),
    path('good_image/', views.good_image, name='good_image'),
]