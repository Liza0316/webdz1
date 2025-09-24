from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    output = ", ".join([p.name for p in products])
    return HttpResponse(f"Товари: {output}")

def index(request):
    return HttpResponse("Вітаю! Це головна сторінка магазину.")