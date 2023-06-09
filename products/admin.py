from django.contrib import admin
from .models import Product, Category, Brand, Type


class ProductAdmin(admin.ModelAdmin):
    """ Admin panel configuration for products """
    search_fields = ['name', 'category', 'brand', 'type']
    list_display = (
        'sku',
        'name',
        'description',
        'category',
        'brand',
        'type',
        'price',
        'image',
    )

    ordering = ('brand',)


class CategoryAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the category of products """
    list_display = (
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the brand of products """
    list_display = (
        'name',
    )

    ordering = ('name',)


class TypeAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the application type of products """
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Type, TypeAdmin)
