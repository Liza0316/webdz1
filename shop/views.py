from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse("Вітаю! Це головна сторінка магазину.")

def product_list(request):
    products = Product.objects.all()
    if products.exists():
        output = ", ".join([f"{p.name} ({p.price} грн, Категорія: {p.category.name})" for p in products])
        return HttpResponse(f"Товари: {output}")
    else:
        return HttpResponse("Продуктів поки немає")
