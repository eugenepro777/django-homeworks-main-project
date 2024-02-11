import csv
from django.contrib import admin
from django.http import HttpResponse

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_amount', 'order_date']
    list_filter = ['order_date', 'customer']
    readonly_fields = ['order_date', 'total_amount']
    search_fields = ['id', 'total_amount']
    search_help_text = 'Поиск заказа по номеру и сумме'
    actions = ['export_to_csv']
    fieldsets = [
        ('Основная информация', {
            'fields': ['customer', 'total_amount', 'order_date']
        }),
        ('Товары', {
            'fields': ('products',)
        })
    ]
    filter_horizontal = ('products',)

    # здесь встраиваем действие 'Экспорт в CSV' внутрь класса, как его метод, modeladmin не нужен
    @admin.action(description='Экспорт в CSV')
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Клиент', 'Сумма заказа', 'Дата заказа'])

        for order in queryset:
            writer.writerow([order.id, order.customer.name, order.total_amount, order.order_date])
        return response
