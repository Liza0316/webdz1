from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'category')
    list_filter = ['category']
    list_editable = ['price', 'category'] 
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)