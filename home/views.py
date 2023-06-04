from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    Displays the home page
    """
    template_name = 'home/index.html'
