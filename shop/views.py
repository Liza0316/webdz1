from django.shortcuts import render 
from .models import Product, Category 
def product_list_view(request):
    """ Ця функція відповідає за сторінку зі списком усіх товарів."""

    all_products = Product.objects.all()
    context = {
        'products': all_products,
    }
    
    return render(request, 'shop/product_list.html', context)

def category_list_view(request):
    """Ця функція відповідає за сторінку зі списком усіх категорій."""

    all_categories = Category.objects.all()
    
    context = {
        'categories': all_categories, 
    }
    
    return render(request, 'shop/category_list.html', context)