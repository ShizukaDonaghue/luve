from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<slug:slug>/', views.edit_article, name='edit_article'),
    path('delete/<slug:slug>/', views.delete_article, name='delete_article'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
    path('like/<slug:slug>/', views.article_like, name="article_like"),
]
