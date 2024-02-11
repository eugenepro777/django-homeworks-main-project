from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Для списка клиентов"""
    list_display = ['name', 'email', 'phone_number', 'address']
    readonly_fields = ['registration_date']
    search_fields = ['phone_number']
    search_help_text = 'Поиск клиента по номеру телефона'
    """Для отдельного клиента"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Контакты',
            {
                'description': 'Контактная информация клиента',
                'fields': ['phone_number', 'email'],
            },
        ),
        (
            'Адрес',
            {
                'classes': ['collapse'],
                'description': 'Адрес для доставки',
                'fields': ['address'],
            }
        ),
    ]
