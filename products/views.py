from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from .models import Product, Category, Brand, Type


class AllProductsView(generic.ListView):
    """ A view to display all products """

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        """ Returns a list of products based on selected criteria """

        context = super().get_context_data(**kwargs)

        # Checks for search query and set context
        if 'q' in self.request.GET:
            query = self.request.GET.get('q')
            if not query:
                messages.error(
                    self.request, "Please enter your search criteria!")
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            context['products'] = Product.objects.filter(queries)
            context['search_term'] = query

        # Checks for product category selected and set context
        if 'category' in self.request.GET:
            categories = self.request.GET.get('category').split(',')
            context['products'] = Product.objects.filter(
                category__name__in=categories)
            context['current_categories'] = Category.objects.filter(
                name__in=categories)

        # Checks for brand selected and set context
        if 'brand' in self.request.GET:
            brands = self.request.GET.get('brand').split(',')
            context['products'] = Product.objects.filter(
                brand__name__in=brands)

        # Checks for application type selected and set context
        if 'type' in self.request.GET:
            types = self.request.GET.get('type').split(',')
            context['products'] = Product.objects.filter(
                type__name__in=types)

        return context


class ProductDetail(View):
    """ A view to display the product detail """

    def get(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        context = {
            'product': product,
        }
        return render(request, 'products/product_detail.html', context)
