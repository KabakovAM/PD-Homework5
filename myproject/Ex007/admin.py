from django.contrib import admin
from . import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'reg_data']
    ordering = ['name']
    list_filter = ['reg_data']
    search_fields = ['email']
    search_help_text = 'Поиск по Email'
    readonly_fields = ['reg_data']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Доп. инфо.',
            {
                'classes': ['collapse'],
                'fields': ['phone', 'adress', 'reg_data'],
            },
        ),
    ]

class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'reg_data']
    ordering = ['name']
    list_filter = ['price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по названию'
    readonly_fields = ['reg_data']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'quantity'],
            },
        ),
        (
            'Доп. инфо.',
            {
                'classes': ['collapse'],
                'fields': ['description', 'reg_data'],
            },
        ),
                (
            'Фото',
            {
                'classes': ['wide'],
                'fields': ['picture'],
            },
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'total', 'reg_data']
    ordering = ['pk']
    list_filter = ['client', 'reg_data']
    search_fields = ['pk']
    search_help_text = 'Поиск по ID'
    readonly_fields = ['reg_data']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client', 'reg_data', 'total'],
            },
        ),
        (
            'Товары',
            {
                'classes': ['collapse'],
                'fields': ['good'],
            },
        ),
    ]

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Good, GoodAdmin)
admin.site.register(models.Order, OrderAdmin)
