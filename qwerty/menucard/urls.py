from django.urls import path
from . import views

app_name = 'menucard'

urlpatterns = [
    path('menucard/<int:id>',views.home, name='home'),
    path('product/<int:id>',views.products, name='product'),
    path('addtocart/<int:pid>',views.AddToCart, name='addtocart'),
    path('addquantity/', views.addQuantity, name='addquantity'),
    path('lessquantity/', views.lessQuantity, name='lessquantity'),
    path('tablenumber/', views.tableNumber, name='tablenumber'),
    path('cart',views.cart, name='cart'),
    path('deletecart/<int:id>',views.deleteCart, name='deletecart'),
    path('ordersuccess',views.orderSuccess, name='ordersuccess'),
    path('productdata/<int:id>',views.productData, name='productdata'),
]