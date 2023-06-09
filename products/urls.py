from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductsView.as_view(), name='products'),
    path('<product_id>', views.ProductDetail.as_view(), name='product_detail'),
]
