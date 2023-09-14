from django.contrib import admin
from .models import Product, Category, Brand, Type, ProductReview


@admin.register(Product)
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the category of products """
    list_display = (
        'name',
        'display_name',
    )

    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the brand of products """
    list_display = (
        'name',
        'display_name',
    )

    ordering = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """ Admin panel configuration for the application type of products """
    list_display = (
        'name',
        'display_name',
    )

    ordering = ('name',)


@admin.register(ProductReview)
class ReviewAdmin(admin.ModelAdmin):
    """ Admin panel configuration for product reviews """
    list_display = (
        'product', 'name', 'title', 'rating', 'created_on'
    )
    list_filter = (
        'rating',
    )
    search_fields = ['name', 'product', 'rating', 'content']

    ordering = ('-created_on',)
