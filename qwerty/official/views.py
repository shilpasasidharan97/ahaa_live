from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from website.models import FrontBanner, ProductPageBanner, Restaurant
from aahalive.decorators import auth_official
# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request,phone=phone, password=password)
        # print(user)
        if user is not None:
            if user.restaurant:
                login(request, user)
                return redirect('web:home')
            elif user.is_superuser == True:
                login(request, user)
                return redirect('official:home')
            else:
                return redirect('official:loginPage')
        else:
            return redirect('official:loginPage')
    return render(request, 'official/login.html')


@auth_official
@login_required(login_url='/official/login-page')
def home(request): 
    resto_count = Restaurant.objects.all().count() 
    all_resto = Restaurant.objects.all()[:5] 
    context = {
        "is_home":True,
        "resto_count":resto_count,
        "all_resto":all_resto,
    }
    return render(request, 'official/home.html',context)


@auth_official
@login_required(login_url='/official/login-page')
def resturantList(request):
    all_resturants = Restaurant.objects.all().order_by('restaurant_name')
    print(all_resturants)
    context = {
        "is_resto":True,
        "all_resturants":all_resturants,
    }
    return render(request, 'official/resturant_list.html',context)


@auth_official
@login_required(login_url='/official/login-page')
def resturantDetails(request,id):
    resto_details = Restaurant.objects.get(id=id)
    data = {
        'resto_name':resto_details.restaurant_name,
        'creator_name':resto_details.creator_name,
        'email':resto_details.email,
        'phone':resto_details.phone,
        'district':resto_details.district,
        'state':resto_details.state,
        'address':resto_details.address
    }
    return JsonResponse(data)


@auth_official
@login_required(login_url='/official/login-page')
def creatUsers(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        email = request.POST['email']
        district = request.POST['district']
        rname = request.POST['rname']
        phone = request.POST['phone']
        state = request.POST['state']
        address = request.POST['address']
        password = request.POST['password']

        resto_exist = Restaurant.objects.filter(phone=phone).exists()
        if not resto_exist:
            new_resto = Restaurant(creator_name=cname,restaurant_name=rname, email=email,phone=phone,password=password,district=district, state=state, address=address)
            new_resto.save()
            return render(request, 'official/create_user.html',{'status':1,})
        else:
            return render(request, 'official/create_user.html',{'status':0,})
    context = {
        "is_users":True,
    }
    return render(request, 'official/create_user.html',context)

@auth_official
@login_required(login_url='/official/login-page')
def bannerPage(request):
    if request.method == 'POST':
        print('front-image')
        front_image = request.FILES['front-image']
        front_banner = FrontBanner(image=front_image)
        front_banner.save()
    all_front_banner = FrontBanner.objects.all()
    all_product_banner = ProductPageBanner.objects.all()
    context = {
        "is_banner":True,
        "all_front_banner":all_front_banner,
        "all_product_banner":all_product_banner,
    }
    return render(request, 'official/banneradding.html',context)


@auth_official
@login_required(login_url='/official/login-page')
def productBanner(request):
    if request.method == 'POST':
        product_image = request.FILES['product-image']
        product_banner = ProductPageBanner(image=product_image)
        product_banner.save()
    return redirect('official:banneradding')


def logout_resto(request):
    logout(request)
    return redirect('official:loginPage')
