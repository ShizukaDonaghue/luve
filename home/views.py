from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    """ A view to display the home page """

    template_name = 'home/index.html'


class PrivacyPolicy(TemplateView):
    """ A view to display the privacy policy """

    template_name = 'home/privacy_policy.html'


class TermsConditions(TemplateView):
    """ A view to display the terms and conditions """

    template_name = 'home/terms_conditions.html'
