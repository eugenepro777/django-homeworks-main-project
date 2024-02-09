from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


def fetch_product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def fetch_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_list.html', {'product': product})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.image = form.cleaned_data['image']
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity,
            'image': product.image
        })
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

