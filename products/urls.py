from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('addprodsub/', views.add_product_subs, name='add_product_subs'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('editprodsub/', views.edit_product_subs, name='edit_product_subs'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
]