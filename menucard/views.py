from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'menucard/home.html')


def products(request):
    return render(request, 'menucard/product.html')


def cart(request):
    return render(request, 'menucard/cart.html')


def orderSuccess(request):
    return render(request, 'menucard/order-success.html')
