from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import Category, Product, RestaurantQrcode, Restaurant, SubCategory
from django.http import JsonResponse


# Create your views here.


@login_required
def home(request):
    user = request.user
    qr_code = RestaurantQrcode.objects.get(restaurant=user.restaurant)
    context = {
        "is_home":True,
        "qr_code":qr_code,
    }
    return render(request, 'web/home.html', context)


@login_required
def category(request):
    categories = Category.objects.filter(restaurent=request.user.restaurant)
    if request.method == 'POST':
        category_name = request.POST['cat-name']
        category_image = request.POST['cat-image']
        new_category = Category(name=category_name, icon=category_image, restaurent=request.user.restaurant)
        new_category.save()
    else:
        pass
    context = {
        "is_product":True,
        "categories":categories,
    }
    return render(request, 'web/category.html', context)


def categoryNameValidation(request):
    category = request.GET['cat_name']
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


def getCategory(request,id):
    print(id,"#"*20)
    category = Category.objects.get(id=id)
    print(category)
    data = {
        'name':category.name,
        'image':category.icon.url,
    }
    print(data)
    return JsonResponse(data)


def editCategory(request):
    cname = request.POST['name']
    image = request.FILES.get("photo", "Photo Not Uploded")
    id=request.POST['fid']

    cat = Category.objects.get(id=id)
    cat.name = cname
    cat.save()
    if image != "Photo Not Uploded":
        cat.icon=image
        cat.save()
    else:
        pass
    return JsonResponse({'data':'sss'})



def subCategory(request,id):
    subcategories = SubCategory.objects.filter(Category__restaurent=request.user.restaurant, Category=id)
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        subcat_name =request.POST['subcat-name']
        new_subactegory = SubCategory(name=subcat_name, Category=category)
        new_subactegory.save()
    context = {
        "is_product":True,
        "subcategories":subcategories
    }
    return render(request, 'web/subcategory.html', context)


def getSubcategory(request,id):
    subcategory =SubCategory.objects.get(id=id)
    print(subcategory)
    data = {
        'name':subcategory.name
    }
    print(data)
    return JsonResponse(data)


@login_required
def product(request,id):
    products = Product.objects.filter(subcategory__Category__restaurent=request.user.restaurant,subcategory=id)
    # print(products)
    subCategory = SubCategory.objects.get(id=id)
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_ingrediants = request.POST['p_ingrediants']
        product_description = request.POST['p_descriptions']
        product_image = request.FILES['p_image']
        new_product = Product(name=product_name, price=product_price,ingrediants=product_ingrediants, description=product_description, image=product_image,subcategory=subCategory)
        new_product.save()
    context = {
        "is_product":True,
        "products":products,
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