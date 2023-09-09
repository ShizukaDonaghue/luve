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
        )
        widgets = {
            'content': SummernoteWidget(),
        }

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-main'
