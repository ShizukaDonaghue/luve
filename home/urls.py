from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('privacy_policy/',
         views.PrivacyPolicy.as_view(), name='privacy_policy'),
    path('terms_conditions/',
         views.TermsConditions.as_view(), name='terms_conditions'),
]
