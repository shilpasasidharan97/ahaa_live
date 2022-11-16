from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import RestaurantQrcode, Restaurant

# Create your views here.


@login_required
def home(request):
    user = request.user
    print(user,'%'*20)
    qr_code = RestaurantQrcode.objects.get(restaurant=user.restaurant)
    context = {
        "is_home":True,
        "qr_code":qr_code,
    }
    return render(request, 'web/home.html', context)


@login_required
def category(request):
    context = {
        "is_product":True
    }
    return render(request, 'web/category.html', context)


@login_required
def product(request):
    context = {
        "is_product":True
    }
    return render(request, 'web/product.html', context)


@login_required
def profile(request):
    context = {
        "is_profile":True
    }
    return render(request, 'web/profile.html', context)


@login_required
def settings(request):
    context = {
        "is_settings":True
    }
    return render(request, 'web/settings.html', context)