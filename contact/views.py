from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):
    """A view to show the contact page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            query_type = request.POST.get('query_type')
            cust_name = request.POST.get('name')
            cust_email = request.POST.get('email')
            message = request.POST.get('message')

            form.save()
            messages.success(
                request,
                f'Your message has been received. Thank you {cust_name}!')

            # Send the user a confirmation email
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt'
            )
            body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'cust_name': cust_name}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            # Send the store a notification email
            subject = render_to_string(
                'contact/confirmation_emails/customer_query_subject.txt',
                {'query_type': query_type,
                 'cust_name': cust_name}
            )
            body = render_to_string(
                'contact/confirmation_emails/customer_query_body.txt',
                {'query_type': query_type,
                 'cust_name': cust_name,
                 'cust_email': cust_email,
                 'message': message}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is completed fully and try again!')

    else:
        if request.user.is_authenticated:
            # Prepopulate the form with the user name and email address
            form = ContactForm(initial={
                'name': request.user.username,
                'email': request.user.email,
                })
        else:
            form = ContactForm()

    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, 'contact/contact.html', context)
