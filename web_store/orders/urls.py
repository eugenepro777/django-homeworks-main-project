from django.urls import path

from .views import fetch_customer_orders, fetch_ordered_products_by_period, fetch_ordered_products_by_days

urlpatterns = [
    path('customer-orders/<int:customer_id>', fetch_customer_orders, name='customer_orders'),
    path('ordered-products-by-period/<int:customer_id>', fetch_ordered_products_by_period,
         name='ordered_products_by_period'),
    path('ordered-products-by-days/<int:customer_id>/<int:num_days>', fetch_ordered_products_by_days,
         name='ordered_products_by_days')
]
