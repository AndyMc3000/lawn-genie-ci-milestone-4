from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to return the cart template """

    return render(request, 'cart/cart.html')


# copied from Boutique Ado store
def add_to_cart(request, item_id):
    """ Add a quantity of a specific product to the shopping cart, and dispaly toast message """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'You updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'You added size {size.upper()} {product.name} to your shopping cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'You added size {size.upper()} {product.name} to your shopping cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'You updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'You added {product.name} to your shopping cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


# copied from Boutique Ado store
def adjust_cart(request, item_id):
    """Updates the quantity of the specified product in the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'You updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'You removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'You updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'You removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# copied from Boutique Ado store
def remove_from_cart(request, item_id):
    """Removes an item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'You have removed size {size.upper()} {product.name} from your cart.')
        else:
            cart.pop(item_id)
            messages.success(request, f'You have removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was an error removing your item: {e}')
        return HttpResponse(status=500)
