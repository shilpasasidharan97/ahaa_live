from django.urls import path
from . import views

app_name = 'official'

urlpatterns = [
    path('login',views.loginPage, name='login'),
    path('',views.home, name='home'),
    path('resturant_list',views.resturantList, name='resturant_list'), 
    path('create_user',views.creatUsers, name='create_user'), 
]