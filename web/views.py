from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "is_home":True
    }
    return render(request, 'web/home.html', context)


def category(request):
    context = {
        "is_product":True
    }
    return render(request, 'web/category.html', context)


def product(request):
    context = {
        "is_product":True
    }
    return render(request, 'web/product.html', context)


def profile(request):
    context = {
        "is_profile":True
    }
    return render(request, 'web/profile.html', context)


def settings(request):
    context = {
        "is_settings":True
    }
    return render(request, 'web/settings.html', context)