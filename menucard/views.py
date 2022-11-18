from django.shortcuts import render

from website.models import Restaurant, Category
from django.http import JsonResponse

# Create your views here.

def home(request,id):
    resto = Restaurant.objects.get(id=id)
    categories = Category.objects.filter(restaurent=resto)
    context = {
        "categories":categories,
    }
    return render(request, 'menucard/home.html',context)


def products(request):
    return render(request, 'menucard/product.html')




def cart(request):
    return render(request, 'menucard/cart.html')


def orderSuccess(request):
    return render(request, 'menucard/order-success.html')
