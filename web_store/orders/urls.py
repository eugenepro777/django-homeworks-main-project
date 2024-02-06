from django.urls import path

from orders.views import fetch_customer_orders


urlpatterns = [
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
]
