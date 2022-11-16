from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'website/home.html')


def registration(request):
    return render(request,'website/registration.html')