from django.urls import path

from orders.views import fetch_customer_orders, fetch_ordered_products_by_period

urlpatterns = [
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:customer_id>', fetch_ordered_products_by_period,
         name='ordered_products_by_period'),
]
