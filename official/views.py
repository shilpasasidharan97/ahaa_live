from django.shortcuts import render

# Create your views here.


def loginPage(request):
    return render(request, 'official/login.html')


def home(request):
    context = {
        "is_home":True,
    }
    return render(request, 'official/home.html',context)


def resturantList(request):
    context = {
        "is_resto":True,
    }
    return render(request, 'official/resturant_list.html',context)


def creatUsers(request):
    context = {
        "is_users":True,
    }
    return render(request, 'official/create_user.html',context)