from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'№{self.id}, клиент:{self.customer.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
