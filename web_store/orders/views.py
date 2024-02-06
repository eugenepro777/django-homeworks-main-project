from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Customer, Order


def fetch_customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)


# сортировка товаров из заказов - за неделю, месяц, год
def fetch_ordered_products_by_period(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(customer=customer, order_date__gte=week_ago)
    orders_month = Order.objects.filter(customer=customer, order_date__gte=month_ago)
    orders_year = Order.objects.filter(customer=customer, order_date__gte=year_ago)

    products_week = set()
    products_month = set()
    products_year = set()

    for order in orders_week:
        products_week.update(order.products.all())

    for order in orders_month:
        products_month.update(order.products.all())

    for order in orders_year:
        products_year.update(order.products.all())

    context = {
        'customer': customer,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, 'ordered_products_sort.html', context)


# более универсальная функция, задаём количество дней произвольно
def fetch_ordered_products_by_days(request, customer_id, num_days):
    customer = get_object_or_404(Customer, pk=customer_id)
    today = timezone.now().date()
    start_date = today - timedelta(days=num_days)
    orders = Order.objects.filter(customer=customer, order_date__gte=start_date)

    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {
        'customer': customer,
        'products': products,
        'num_days': num_days,
    }
    return render(request, 'ordered_products_sort.html', context)
