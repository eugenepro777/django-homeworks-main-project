from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order


def fetch_orders_for_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer_id)
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)
