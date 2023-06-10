from products.models import Brand


def brands_list(request):
    brands_list = Brand.objects.all()

    context = {
        'brands_list': brands_list,
    }

    return context
