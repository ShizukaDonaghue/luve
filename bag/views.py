from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404,
    )
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity_input = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity_input.isdigit():
        quantity = int(request.POST.get('quantity'))
        # If the order quantity is less than 1
        if quantity < 1:
            messages.error(
                request, f'Sorry, the order quantity must be 1 or more. \
                    Please try again!')
        # If the order quantity is greater than 20
        elif quantity > 20:
            messages.error(
                request, f'Sorry, the maximum quantity per order is 20. \
                    Please try again!')
        # If the item is already in the shopping bag
        elif item_id in list(bag.keys()):
            # If the total order quantity is greater than 20
            if bag[item_id] + quantity > 20:
                messages.error(
                    request, f'Sorry, the maximum quantity per order is 20. \
                        Please try again!')
            # If the total order quantity does not exceed 20
            else:
                bag[item_id] += quantity
                messages.success(
                    request, f'Updated {product.name} quantity to \
                        {bag[item_id]}!')
        # If the item is not yet in the shopping bag
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'{product.name} has been added to your bag!')
    # If the order quantity is less than 0
    elif quantity_input.startswith('-'):
        messages.error(
            request, f'Sorry, the order quantity must be 1 or more. \
                Please try again!')
    # If the order quantity is a floating-point number or other invalid input
    else:
        messages.error(
            request, f'Please enter a whole number!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the products in the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity_input = request.POST.get('quantity')
    bag = request.session.get('bag', {})

    # If the order quantity is a positive integer
    if quantity_input.isdigit():
        quantity = int(request.POST.get('quantity'))
        # If the order quantity is greater than 20
        if quantity > 20:
            messages.error(
                request, f'Sorry, the maximum quantity per order is 20. \
                    Please try again!')
        # If the order quantity is greater than or equal to 1
        elif quantity >= 1:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}!')
        # If the order quantity is 0, the item is removed from the shopping bag
        else:
            bag.pop(item_id)
            messages.success(
                request, f'{product.name} has been removed from your bag.')
    # If the order quantity is less than 0
    elif quantity_input.startswith('-'):
        messages.error(
            request, f'Sorry, the order quantity must be 1 or more. \
                Please try again!')
    # If the order quantity is a floating-point number or other invalid input
    else:
        messages.error(
            request, f'Please enter a whole number!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
