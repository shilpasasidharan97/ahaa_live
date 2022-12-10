from .models import FrontBanner
from .models import JsonResponse
from .models import ProductPageBanner
from .models import Restaurant
from .models import Video
from menucard.decorators import auth_official
from .models import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render


# LOGIN
def loginPage(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        password = request.POST["password"]
        user = authenticate(request, phone=phone, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("web:home")
        else:
            return redirect("official:loginPage")
    return render(request, "official/login.html")


def home(request):
    context = {"is_home": True}
    return render(request, "official/home.html", context)


# RESTURANT LIST
@auth_official
@login_required(login_url="/official/login-page")
def resturantList(request):
    context = {"is_resto": True}
    return render(request, "official/resturant_list.html", context)


# RESTURANT DETAILS
@auth_official
@login_required(login_url="/official/login-page")
def resturantDetails(request, id):
    resto_details = Restaurant.objects.get(id=id)
    data = {
        "resto_name": resto_details.restaurant_name,
        "creator_name": resto_details.creator_name,
        "email": resto_details.email,
        "phone": resto_details.phone,
        "district": resto_details.district,
        "state": resto_details.state,
        "address": resto_details.address,
    }
    return JsonResponse(data)


# USER CREATION
@auth_official
@login_required(login_url="/official/login-page")
def creatUsers(request):
    context = {"is_users": True}
    return render(request, "official/create_user.html", context)


# BANNER SECTION
@auth_official
@login_required(login_url="/official/login-page")
def bannerPage(request):
    if request.method == "POST":
        print("front-image")
        front_image = request.FILES["front-image"]
        front_banner = FrontBanner(image=front_image)
        front_banner.save()
    all_front_banner = FrontBanner.objects.all()
    all_product_banner = ProductPageBanner.objects.all()
    context = {"is_banner": True, "all_front_banner": all_front_banner, "all_product_banner": all_product_banner}
    return render(request, "official/banneradding.html", context)


# PRODUCT BANNER
@auth_official
@login_required(login_url="/official/login-page")
def productBanner(request):
    if request.method == "POST":
        product_image = request.FILES["product-image"]
        product_banner = ProductPageBanner(image=product_image)
        product_banner.save()
    return redirect("official:banneradding")


# VIDEO
def videoAdding(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        video = request.FILES["video"]
        new_video = Video(video=video)
        new_video.save()
    context = {"is_video": True, "all_video": all_video}
    return render(request, "official/video.html", context)


# LOGOUT
def logout_resto(request):
    logout(request)
    return redirect("official:loginPage")
