from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from .models import Product, Category, Brand, Type, ProductReview
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    current_categories = None
    brands = None
    current_brands = None
    sort = None
    direction = None

    if request.GET:
        # Check for a search query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'Please enter your search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        # Check if a product category selected
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            current_categories = Category.objects.filter(name__in=categories)

        # Check if a product brand selected
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            current_brands = Brand.objects.filter(name__in=brands)

        # Check if a product type selected
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(type__name__in=types)
            current_types = Type.objects.filter(name__in=types)

        # Check if a sorting order selected
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
        'current_brands': current_brands,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.order_by('created_on')

    context = {
        'product': product,
        'reviews': reviews,
        'form': ReviewForm()
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_review(request, product_id):
    """ A view to add a product review """

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.name = request.user
                review.save()
                messages.success(
                    request, 'Your review has been added successfully!')
                return HttpResponseRedirect(
                    reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add your review. \
                    Please check the details and try again!')
    else:
        messages.error(request, 'Please log in to leave a review!')


@login_required
def edit_review(request, review_id):
    """ A view to edit a product review """

    review = get_object_or_404(ProductReview, pk=review_id)

    if not review.name == request.user:
        messages.error(
            request, 'Sorry, you are not authorised to edit this review.')
        return redirect(reverse('product_detail', args=[review.product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your review has been updated successfully!')
            return HttpResponseRedirect(
                reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(request, 'Failed to update your review. \
                Please check the details and try again!')
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {review.product.name}'
            )

    template = 'products/edit_review.html'
    context = {
        'review': review,
        'form': form
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ A view to delete a product review """

    review = get_object_or_404(ProductReview, pk=review_id)

    if review.name == request.user:
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect(reverse('product_detail', args=[review.product.id]))
    else:
        messages.error(
            request, 'Sorry, you are not authorised to delete this review.')
        return redirect(reverse('product_detail', args=[review.product.id]))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, you are not authorised to add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'{product.name} has been added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add a product. \
                    Please double-check the details and try again!')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, you are not authorised to edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'{product.name} has been updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to edit the product. \
                    Please double-check the details and try again!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}.')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_staff:
        messages.error(
            request, 'Sorry, you are not authorised to delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been deleted!')
    return redirect(reverse('products'))
