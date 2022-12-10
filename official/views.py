from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render


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


def resturantList(request):
    context = {"is_resto": True}
    return render(request, "official/resturant_list.html", context)


def creatUsers(request):
    context = {"is_users": True}
    return render(request, "official/create_user.html", context)


def logout_resto(request):
    logout(request)
    return redirect("official:loginPage")
