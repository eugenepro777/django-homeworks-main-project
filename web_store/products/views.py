from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)
