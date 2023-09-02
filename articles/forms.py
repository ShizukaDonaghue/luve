from django import forms
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from .models import Article


class ArticleForm(forms.ModelForm):
    """ Form used to post an article """
    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'content',
            'image',
            'status',
        )
        widgets = {
            'content': SummernoteWidget(),
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
