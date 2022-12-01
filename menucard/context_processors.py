from website.models import Category, Product, Restaurant, RestoSave, SocialMediaLink, User,CartItems, Video

# def main_context(request):
#     if request.session.exists(request.session.session_key):
#         cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
#         return {
#             "domain": request.META["HTTP_HOST"],
#             "cart_items_count":cart_items,
#         }
#     else:
#         return {
#             "domain": request.META["HTTP_HOST"],
#         }



# def main_context(request):
#     if request.session.exists(request.session.session_key):
#         cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
#         resto = RestoSave.objects.get(user_session_id=request.session.session_key)
#         return {
#             "domain": request.META["HTTP_HOST"],
#             "cart_items_count":cart_items,
#             "resto":resto,
#         }
#     else:
#         return {
#             "domain": request.META["HTTP_HOST"],
#         }




def main_context(request):
    if request.session.exists(request.session.session_key):
        cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
        video = Video.objects.all().last()
        try:
            resto = RestoSave.objects.get(user_session_id=request.session.session_key)
            rest= resto.resto_pk
            resturants_obj = Restaurant.objects.get(id=rest)
            print(resturants_obj.is_table,"#"*20)
            # eeemail = resturants_obj.email
            # print(aaa,'12'*20)
            # categories = Category.objects.filter(restaurent__id=resto.resto_pk)
            all_products = Product.objects.select_related('subcategory').filter(subcategory__Category__restaurent=resto.resto_pk).values('subcategory__Category__name','subcategory__Category__icon','subcategory__Category__id').distinct()
            if SocialMediaLink.objects.filter(resturant__id=rest).exists():
                links = SocialMediaLink.objects.get(resturant__id=rest)
            else:
                pass
            return {
                "domain": request.META["HTTP_HOST"],
                "cart_items_count":cart_items,
                "resto":resto,
                "all_products":all_products,
                "video":video,
                "links":links,
                "resturants_obj":resturants_obj,
                # "eeemail":eeemail,
            }
        except :
            return {
                "domain": request.META["HTTP_HOST"],
                "cart_items_count":cart_items,
                "video":video,
                # "eeemail":eeemail,
            }
    else:
        return {
            "domain": request.META["HTTP_HOST"],
        }
