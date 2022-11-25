from django.contrib import admin

from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','phone')
    search_fields=('phone',)
admin.site.register(User,UserAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id','restaurant_name','creator_name','email','phone')
    search_fields=('phone',)
admin.site.register(Restaurant,RestaurantAdmin)


admin.site.register(DefaultCats)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','restaurent','name',)
    search_fields=('name',)
admin.site.register(Category,CategoryAdmin)


admin.site.register(RestaurantQrcode)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Category','name',)
    search_fields=('name',)
admin.site.register(SubCategory,SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('subcategory','name',)
    search_fields=('name',)
admin.site.register(Product,ProductAdmin)

admin.site.register(Cart)


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity', 'total')
    search_fields=('product','quantity', 'total')
admin.site.register(CartItems,CartItemsAdmin)


admin.site.register(FrontBanner)


admin.site.register(ProductPageBanner)







