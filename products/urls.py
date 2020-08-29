from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('addprodsub/', views.add_product_subs, name='add_product_subs'),
    path('joinprodsub/', views.join_product_and_subs, name='join_product_and_subs'),
]