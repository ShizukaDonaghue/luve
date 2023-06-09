from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Category, Brand, Type


class AllProductsView(generic.ListView):
    """ A view to display all products """

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 12


class ProductDetail(View):
    """ A view to display the product detail """

    def get(self, request, product_id, *args, **kwargs):

        product = get_object_or_404(Product, pk=product_id)

        context = {
            'product': product,
        }

        return render(request, 'products/product_detail.html', context)
