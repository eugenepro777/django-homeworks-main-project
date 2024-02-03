from faker import Faker
from customers.models import Customer
from products.models import Product
from orders.models import Order

fake = Faker()

"""
Исключительно для генерации тестовых данных, локаль выбирается передачей в Faker() строки. По умолчанию: 'en-EN',
для кириллицы передать 'ru-RU'
Запуск через python manage.py shell
В shell делаем импорт: from utils import create_fake_customers, create_fake_products, create_fake_orders
потом вызов функции с передачей нужного количества клиентов, товаров и заказов:
>>> create_fake_customers()
>>> create_fake_products()
>>> create_fake_orders()
"""


def create_fake_customers(num_customers):
    for _ in range(num_customers):
        customer = Customer(
            name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            registration_date=fake.date_this_year()
        )
        customer.save()


def create_fake_products(num_products):
    for _ in range(num_products):
        product = Product(
            name=fake.word().capitalize(),
            description=fake.text(),
            price=fake.random_number(digits=3),
            quantity=fake.random_number(digits=2),
            added_date=fake.date_this_year()
        )
        product.save()


def create_fake_orders(num_orders):
    for _ in range(num_orders):
        customer = Customer.objects.order_by('?').first()
        products = Product.objects.order_by('?')[:3]
        total_amount = sum(product.price for product in products)
        order_date = fake.date_this_year()

        order = Order.objects.create(
            customer=customer,
            total_amount=total_amount,
            order_date=order_date
        )
        order.products.set(products)
