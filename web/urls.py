from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.home,name='home'),
    path('category',views.category,name='category'),
    path('product',views.product,name='product'),
    path('profile',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),
]