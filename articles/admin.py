from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    """ Admin panel configuration for articles """
    search_fields = ['title', 'description', 'author']
    list_display = (
        'title',
        'author',
        'description',
        'created_on',
    )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')

    ordering = ('-created_on',)


admin.site.register(Article, ArticleAdmin)
