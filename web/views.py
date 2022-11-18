from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import Category, RestaurantQrcode, Restaurant
from django.http import JsonResponse


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
    if request.method == 'POST':
        category_name = request.POST['cat-name']
        category_image = request.POST['cat-image']
        new_category = Category(name=category_name, icon=category_image, restaurent=request.user.restaurant)
        new_category.save()
        print(new_category, '%'*19)
    else:   
        print('%'*1)
        pass
    context = {
        "is_product":True
    }
    return render(request, 'web/product.html', context)


def categoryNameValidation(request):
    category = request.GET['cat_name']
    print(category)
    if Category.objects.filter(name=category).exists():
        data = {
            'msg':'Category alerdy exists'
        }
        return JsonResponse(data)
    else:
        data ={
            'sss':'sss'
        }
        return JsonResponse(data)



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