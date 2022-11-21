from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(User)

admin.site.register(Cart)

admin.site.register(DefaultCats)

admin.site.register(RestaurantQrcode)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name','creator_name','email','phone')
    search_fields=('phone',)
admin.site.register(Restaurant,RestaurantAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('restaurent','name',)
    search_fields=('name',)
admin.site.register(Category,CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('Category','name',)
    search_fields=('name',)
admin.site.register(SubCategory,SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('subcategory','name',)
    search_fields=('name',)
admin.site.register(Product,ProductAdmin)

# class RestaurantQrcodeAdmin(admin.ModelAdmin):
#     list_display = ('restaurent','image',)
#     search_fields=('restaurent',)
# admin.site.register(RestaurantQrcode,RestaurantQrcodeAdmin)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product','quantity', 'total')
    search_fields=('product','quantity', 'total')
admin.site.register(CartItems,CartItemsAdmin)




