from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('dashboard/', views.article_dashboard,
         name='article_dashboard'),
    path('add/', views.add_article, name='add_article'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('like/<slug:slug>/', views.article_like, name="article_like"),
]
