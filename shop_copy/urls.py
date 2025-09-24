from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_copy'),
    path('products/', views.product_list, name='product_list_copy'),
]
