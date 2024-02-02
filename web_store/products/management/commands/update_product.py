from decimal import Decimal
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Update a product info by id. Price in Decimal"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product ID')
        parser.add_argument('description', type=str, help='Product ID')
        parser.add_argument('price', type=Decimal().quantize(Decimal('.01')), help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully updated product: {product}'))