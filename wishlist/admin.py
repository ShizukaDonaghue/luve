from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """ Admin panel configuration for wishlist """
    list_display = (
        'user',
        'product',
    )

    ordering = ('user',)


admin.site.register(Wishlist, WishlistAdmin)
