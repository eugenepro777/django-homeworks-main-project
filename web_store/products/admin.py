from django.contrib import admin

from .models import Product


# здесь действие 'Обнулить товарный остаток' идет отдельной задекорированной функцией, modeladmin - обязательно!
@admin.action(description="Обнулить товарный остаток")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Для списка товаров"""
    list_display = ['name', 'price', 'quantity']
    list_filter = ['added_date', 'price']
    readonly_fields = ['added_date']
    search_fields = ['description']
    search_help_text = 'Поиск товара по описанию'
    actions = [reset_quantity]
    """Для отдельного товара"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Отдел закупок',
            {
                'fields': ['quantity', 'price'],
                'description': 'Для управления товарными запасами'
            },
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Подробная информация о товаре',
                'fields': ['description'],
            }
        ),
        (
            'Изображение товара',
            {
                'description': 'Изображение товара',
                'fields': ['image'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дата добавления',
                'fields': ['added_date'],
            }
        ),
    ]
