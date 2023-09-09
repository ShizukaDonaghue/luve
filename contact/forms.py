from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form for customer messages """

    class Meta:
        model = Contact
        fields = ('query_type', 'name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message',
        }

        self.fields['query_type'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'query_type':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'contact-us'
            self.fields[field].label = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-main'
