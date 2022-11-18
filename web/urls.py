from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.home,name='home'),
    path('category',views.category,name='category'),
    path('categorynamevalidation',views.categoryNameValidation,name='categorynamevalidation'),
    path('subcategory/<int:id>',views.subCategory,name='subcategory'),
    path('product/<int:id>',views.product,name='product'),
    path('profile',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),
]