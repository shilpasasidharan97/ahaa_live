from django.shortcuts import render,redirect
from .models import Restaurant, DefaultCats, Category, RestaurantQrcode
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request,'website/home.html')


def registration(request):
    if request.method == "POST":
        creater_name = request.POST['creater_name']
        resturant_name = request.POST['resturant_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        district = request.POST['district']
        state = request.POST['state']
        address = request.POST['address']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if not Restaurant.objects.filter(phone=phone_number).exists():
            new_resto = Restaurant(creator_name=creater_name,restaurant_name=resturant_name,email=email,phone=phone_number,password=password,district=district,state=state,address=address)
            new_resto.save()
            User = get_user_model()
            User.objects.create_user(phone=phone_number, password=password,restaurant=new_resto)
            user = authenticate(request,phone=phone_number,password=password)
            default_cats = DefaultCats.objects.all()
            url = "https://aahamenu.geany.website/menucard/"+str(new_resto.id)
            RestaurantQrcode.objects.create(restaurant=new_resto,resto_url=url)
            for i in default_cats:
                category_obj = Category(restaurent=new_resto,name=i.no,icon=i.image)
                category_obj.save()
            if user is not None:
                login(request, user)
                return redirect('web:home')
            else:
                print("Not authenticated","*"*3)
    return render(request,'website/registration.html')