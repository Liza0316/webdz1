from django.urls import path
from . import views  
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('products/add/', views.product_create_view, name='product-create'),
    path('categories/add/', views.category_create_view, name='category-create'),
    path('products/<slug:slug>/', views.product_detail_view, name='product-detail'),
    path('categories/<slug:slug>/', views.category_detail_view, name='category-detail'),
    path('products/<slug:slug>/edit/', views.product_update_view, name='product-update'),
    path('categories/<slug:slug>/edit/', views.category_update_view, name='category-update'),
    path('products/<slug:slug>/delete/', views.product_delete_view, name='product-delete'),
    path('categories/<slug:slug>/delete/', views.category_delete_view, name='category-delete'),
]