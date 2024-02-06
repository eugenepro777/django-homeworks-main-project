from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order


def fetch_customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer_id)
    context = {
        'customer': customer,
        'orders': orders,
    }
    return render(request, 'orders/orders.html', context)


def customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id).prefetch_related('products')
    return render(request, 'orders/customer_orders.html', {'customer_orders': customer_orders})
