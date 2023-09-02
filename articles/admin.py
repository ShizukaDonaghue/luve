from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """ Admin panel configuration for articles """
    search_fields = ['title', 'description', 'author']
    list_display = (
        'title',
        'author',
        'description',
        'status',
        'created_on',
    )
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

    ordering = ('-created_on',)


admin.site.register(Article, ArticleAdmin)
