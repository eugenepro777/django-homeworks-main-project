from django.db import models
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    products = models.ManyToManyField(Product, verbose_name='Товары')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'№ {self.pk}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.total_amount = sum(product.price for product in self.products.all())
            # super().save(*args, **kwargs)  # Сохранение заказа для получения значения id
        # self.total_amount = sum(product.price for product in self.products.all())
        super().save(*args, **kwargs)

    def update_total_amount(self):
        self.total_amount = self.products.aggregate(total=models.Sum('price'))['total']
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
