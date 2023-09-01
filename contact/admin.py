from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Admin panel configuration for contact messages """
    search_fields = ['query_type', 'name', 'email']
    list_display = (
        'name',
        'email',
        'query_type',
        'date'
    )

    ordering = ('-date',)


admin.site.register(Contact, ContactAdmin)
