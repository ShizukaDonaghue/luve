from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """ A view to display wishlist """
    wishlist = Wishlist.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a product to wishlist """
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        try:
            wishlist = Wishlist.objects.get(
                user=request.user, product=product)
            if wishlist:
                messages.info(
                    request, f'{product.name} is already in your wishlist!')
        except Wishlist.DoesNotExist:
            Wishlist.objects.create(user=request.user, product=product)
            messages.success(
                request, f'{product.name} has been added to your wishlist!')
        finally:
            return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, wishlist_id):
    """ A view to remove a product from wishlist on wishlist page """
    if request.method == 'POST':
        wishlist = Wishlist.objects.get(id=wishlist_id)
        wishlist.delete()
        messages.success(request, f'{wishlist.product.name} \
            has been removed from your wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist_all(request, product_id):
    """
    A view to remove a product from wishlist on all products page
    """
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        user = request.user
        wishlist = Wishlist.objects.filter(product=product, user=user)
        wishlist.delete()
        messages.success(request, f'{product.name} \
            has been removed from your wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))
