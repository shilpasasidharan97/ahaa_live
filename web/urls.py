from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.home,name='home'),

    # catagory 
    path('category',views.category,name='category'),
    path('categorynamevalidation',views.categoryNameValidation,name='categorynamevalidation'),
    path('getcategory/<int:id>',views.getCategory,name='getcategory'),
    path('editcategory', views.editCategory, name='editcategory'),
    path('deletecatgory/<int:id>', views.deleteCategory, name='deletecatgory'),

    #subcategory 
    path('subcategory/<int:id>',views.subCategory,name='subcategory'),
    path('getsubcategory/<int:id>',views.getSubcategory,name='getsubcategory'),
    path('deletesubcatgory/<int:id>', views.deleteSubCategory, name='deletesubcatgory'),

    path('product/<int:id>',views.product,name='product'),
    path('product-show/<int:id>',views.productshow,name='productshow'),
    path('productinactive/<int:id>', views.productNotavailable, name="productinactive"),
    path('productactive/<int:id>', views.productavailable, name="productactive"),
    path('deleteproduct/<int:id>', views.deleteProduct, name='deleteproduct'),

    path('banner',views.banner,name='banner'),

    path('profile',views.profile,name='profile'),
    path('settings',views.settings,name='settings'),

    path('socialmedia',views.socialMedialinks,name='socialmedia'),
]