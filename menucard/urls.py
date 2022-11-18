from django.urls import path
from . import views

app_name = 'menucard'

urlpatterns = [
    path('menucard/<int:id>',views.home, name='home'),
    path('product/<int:id>',views.products, name='product'),
    path('cart',views.cart, name='cart'),
    path('ordersuccess',views.orderSuccess, name='ordersuccess'),
]