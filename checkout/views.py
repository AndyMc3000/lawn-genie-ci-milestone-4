from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


# copied from Boutique Ado
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your shopping cart.")
        return redirect(reverse('products'))

    # Stripe
    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JRFUVIsoUVtcqqdAnF9QmSQ0cxIrv0qP0F0OYDyqMtv6vagiw77mrEAh8kwtUYWbvj0RetU0l3kcopD3EvZkFZc00VNdnfiRE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
