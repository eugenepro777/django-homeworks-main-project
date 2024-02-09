from django.urls import path

from .views import add_product, fetch_product, fetch_product_list, edit_product

urlpatterns = [
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('product_list/', fetch_product_list, name='product_list'),
    path('<int:product_id>/', fetch_product, name='product_view'),
]
