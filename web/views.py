from website.models import Category
from website.models import Product
from website.models import RestaurantQrcode
from website.models import SubCategory

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

@auth_restaurant
@login_required(login_url='/official/login-page')
def home(request):
    user = request.user
    print(user, "%" * 20)
    qr_code = RestaurantQrcode.objects.get(restaurant=user.restaurant)
    context = {"is_home": True, "qr_code": qr_code}
    return render(request, "web/home.html", context)


@auth_restaurant
@login_required(login_url='/official/login-page')
def category(request):
    categories = Category.objects.filter(restaurent=request.user.restaurant)
    print(categories)
    if request.method == "POST":
        category_name = request.POST["cat-name"]
        category_image = request.POST["cat-image"]
        new_category = Category(name=category_name, icon=category_image, restaurent=request.user.restaurant)
        new_category.save()
    else:
        pass
    context = {"is_product": True, "categories": categories}
    return render(request, "web/category.html", context)


def categoryNameValidation(request):
    category = request.GET["cat_name"]
    if Category.objects.filter(name=category).exists():
        data = {"msg": "Category alerdy exists"}
        return JsonResponse(data)
    else:
        data = {"sss": "sss"}
        return JsonResponse(data)


def subCategory(request, id):
    subcategories = SubCategory.objects.filter(Category__restaurent=request.user.restaurant, Category=id)
    category = Category.objects.get(id=id)
    if request.method == "POST":
        subcat_name = request.POST["subcat-name"]
        new_subactegory = SubCategory(name=subcat_name, Category=category)
        new_subactegory.save()
    context = {"is_product": True, "subcategories": subcategories}
    return render(request, "web/subcategory.html", context)


@login_required
def product(request, id):
    products = Product.objects.filter(subcategory__Category__restaurent=request.user.restaurant, subcategory=id)
    print(products)
    subCategory = SubCategory.objects.get(id=id)
    if request.method == "POST":
        product_name = request.POST["p_name"]
        product_price = request.POST["p_price"]
        product_ingrediants = request.POST["p_ingrediants"]
        product_description = request.POST["p_descriptions"]
        product_image = request.FILES["p_image"]
        new_product = Product(
            name=product_name, price=product_price, ingrediants=product_ingrediants, description=product_description, image=product_image, subcategory=subCategory
        )
        new_product.save()
    context = {"is_product": True}
    return render(request, "web/product.html", context)


# product show modal 
def productshow(request,id):
    product = Product.objects.get(id=id)
    data = {
        "name":product.name,
        "price":product.price,
        "ingrediants":product.ingrediants,
        "description":product.description,
        "image":product.image.url,
    }
    return JsonResponse(data)


@auth_restaurant
@login_required(login_url='/official/login-page')
def banner(request):
    all_banner = RestoBanner.objects.filter(resto=request.user.restaurant).all()
    if request.method == 'POST':
        resto_banner = request.FILES['home-image']
        new_banner =  RestoBanner(image=resto_banner, resto=request.user.restaurant)
        new_banner.save()
    context = {
        "is_banner":True,
        "all_banner":all_banner,
    }
    return render(request, 'web/banner.html',context)



@auth_restaurant
@login_required(login_url='/official/login-page')
def profile(request):
    context = {"is_profile": True}
    return render(request, "web/profile.html", context)


@auth_restaurant
@login_required(login_url='/official/login-page')
def settings(request):
    context = {"is_settings": True}
    return render(request, "web/settings.html", context)
