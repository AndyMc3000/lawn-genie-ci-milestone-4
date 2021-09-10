from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return the 'all products' template, and to allow for searching and sorting of products """

    # Returns all products from the database
    products = Product.objects.all()

    context = {
        'products': products,
    }
   
    return render(request, 'products/products.html', context)
