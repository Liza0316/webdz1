from django.urls import path
from . import views  

urlpatterns = [
    path('products/', views.product_list_view, name='product-list'),
    path('categories/', views.category_list_view, name='category-list'),
]