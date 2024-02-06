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


def fetch_ordered_products_by_time(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(customer=request.user, created_at__gte=week_ago)
    orders_month = Order.objects.filter(customer=request.user, created_at__gte=month_ago)
    orders_year = Order.objects.filter(customer=request.user, created_at__gte=year_ago)

    context = {
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }

    return render(request, 'ordered_products_sort.html', context)
