from website.models import Category
from website.models import Product
from website.models import Restaurant
from website.models import SubCategory

from django.shortcuts import render


def home(request, id):
    resto = Restaurant.objects.get(id=id)
    categories = Category.objects.filter(restaurent=resto)
    context = {"categories": categories}
    return render(request, "menucard/home.html", context)


def products(request, id):
    subcategories = SubCategory.objects.filter(is_active=True, Category=id)
    print(subcategories, "@" * 10)
    products = Product.objects.filter(subcategory__Category__id=id)
    print(products)
    context = {"subcategories": subcategories, "products": products}
    return render(request, "menucard/product.html", context)


def cart(request):
    return render(request, "menucard/cart.html")


def orderSuccess(request):
    return render(request, "menucard/order-success.html")
