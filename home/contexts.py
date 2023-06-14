from products.models import Brand


def brands_list(request):
    """ Makes the list of brands available to all templates for the navbar """
    brands_list = Brand.objects.all()

    context = {
        'brands_list': brands_list,
    }

    return context
