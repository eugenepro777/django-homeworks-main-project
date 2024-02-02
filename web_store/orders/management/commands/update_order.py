from django.core.management.base import BaseCommand
from orders.models import Order
from customers.models import Customer
from products.models import Product


# python manage.py update_order <order_id> <customer_id> <product_id_1> <product_quantity_1> <product_id_2> <product_quantity_2> ...

class Command(BaseCommand):
    help = "Update an order"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='ID of the order to update')
        parser.add_argument('customer_id', type=int, help='ID of the new customer')
        parser.add_argument('product_ids', type=int, nargs='+', help='IDs of the products to add to the order')
        parser.add_argument('quantities', type=int, nargs='+', help='Quantities corresponding to the products')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        customer_id = kwargs['customer_id']
        product_ids = kwargs['product_ids']
        quantities = kwargs['quantities']

        # проверяем есть ли у нас заказ и пользователь с заданным id
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Order with ID {order_id} does not exist'))
            return
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Customer with ID {customer_id} does not exist'))
            return

        order.customer = customer
        # обнуляем сумму заказа перед добавлением новых товаров
        order.total_amount = 0
        order.save()

        order.products.clear()
        for product_id, quantity in zip(product_ids, quantities):
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist'))
                return

            order.products.add(product, through_defaults={'quantity': quantity})
            order.total_amount += product.price * quantity

            self.stdout.write(self.style.ERROR(f'Successfully updated order: {order}'))
