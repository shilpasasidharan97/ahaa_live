from .models import Category
from .models import DefaultCats
from .models import Product
from .models import Restaurant
from .models import RestaurantQrcode
from .models import SubCategory
from .models import User
from django.contrib import admin


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','phone')
    search_fields=('phone',)
admin.site.register(User,UserAdmin)



class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("restaurant_name", "creator_name", "email", "phone")
    search_fields = ("phone",)


admin.site.register(Restaurant, RestaurantAdmin)



admin.site.register(DefaultCats)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("restaurent", "name")
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


admin.site.register(RestaurantQrcode)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("Category", "name")
    search_fields = ("name",)


admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("subcategory", "name")
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)

# class RestaurantQrcodeAdmin(admin.ModelAdmin):
#     list_display = ('restaurent','image',)
#     search_fields=('restaurent',)
# admin.site.register(RestaurantQrcode,RestaurantQrcodeAdmin)
