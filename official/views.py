from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from aahalive.decorators import auth_official
from website.models import FrontBanner, ProductPageBanner, Restaurant
# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request,phone=phone, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('web:home')
        else:
            return redirect('official:loginPage')
    return render(request, 'official/login.html')



def home(request):
    
    context = {
        "is_home":True,
    }
    return render(request, 'official/home.html',context)



def resturantList(request):
    all_resturants = Restaurant.objects.all().order_by('restaurant_name')
    print(all_resturants)
    context = {
        "is_resto":True,
        "all_resturants":all_resturants,
    }
    return render(request, 'official/resturant_list.html',context)



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


def bannerPage(request):
    if request.method == 'POST':
        print('post')
        if 'pbanner' in request.POST:
            print('front-image')
            front_image = request.FILES['front-image']
            front_banner = FrontBanner(image=front_image)
            front_banner.save()
        elif 'fbanner' in request.POST:
            print('product-image')
            product_image = request.FILES['product-image']
            product_banner = ProductPageBanner(image=product_image)
            product_banner.save()
    else:
        print('else')
        pass
    all_front_banner = FrontBanner.objects.all()
    all_product_banner = ProductPageBanner.objects.all()
    context = {
        "all_front_banner":all_front_banner,
        "all_product_banner":all_product_banner,
    }
    return render(request, 'official/banneradding.html',context)


def logout_resto(request):
    logout(request)
    return redirect('official:loginPage')
