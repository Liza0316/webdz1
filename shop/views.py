from django.views.generic import ListView
from .models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CategoryForm 
from django.contrib.auth.decorators import login_required, permission_required 

class ProductListView(ListView):
    model = Product                 
    template_name = 'shop/product_list.html'  
    context_object_name = 'products'  
    paginate_by = 5                     

class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'
    paginate_by = 10                        

@permission_required('shop.add_product', raise_exception=True) 
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

@permission_required('shop.add_category', raise_exception=True) 
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'shop/category_form.html', {'form': form})


def product_detail_view(request, slug): 
    product = get_object_or_404(Product, slug=slug) 
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)

def category_detail_view(request, slug):
    category = get_object_or_404(Category, slug=slug) 
    products = category.products.all() 
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/category_detail.html', context)

@permission_required('shop.change_product', raise_exception=True) 
def product_update_view(request, slug): 
    product = get_object_or_404(Product, slug=slug) 
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save() 
            return redirect('product-detail', slug=product.slug) 
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form})

@permission_required('shop.change_category', raise_exception=True)
def category_update_view(request, slug):
    category = get_object_or_404(Category, slug=slug) 
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save() 
            return redirect('category-list') 
    else:
        form = CategoryForm(instance=category)
    return render(request, 'shop/category_form.html', {'form': form})

@permission_required('shop.delete_product', raise_exception=True) 
def product_delete_view(request, slug):
    product = get_object_or_404(Product, slug=slug) 
    
    if request.method == 'POST':
        product.delete() 
        return redirect('product-list') 
    context = {
        'product': product
    }
    return render(request, 'shop/product_delete.html', context)

@permission_required('shop.delete_category', raise_exception=True) 
def category_delete_view(request, slug): 
    category = get_object_or_404(Category, slug=slug) 
    
    if request.method == 'POST':
        category.delete() 
        return redirect('category-list') 
    context = {
        'category': category
    }
    return render(request, 'shop/category_delete.html', context)