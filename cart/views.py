from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view to retun the cart template """
    
    return render(request, 'cart/cart.html')