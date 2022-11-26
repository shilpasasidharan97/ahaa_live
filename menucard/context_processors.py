from website.models import Category, Product, RestoSave, User,CartItems

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
        try:
            resto = RestoSave.objects.get(user_session_id=request.session.session_key)
            # categories = Category.objects.filter(restaurent__id=resto.resto_pk)
            all_products = Product.objects.select_related('subcategory').filter(subcategory__Category__restaurent=resto.resto_pk).values('subcategory__Category__name','subcategory__Category__icon','subcategory__Category__id').distinct()

            return {
                "domain": request.META["HTTP_HOST"],
                "cart_items_count":cart_items,
                "resto":resto,
                "all_products":all_products,
            }
        except :
            return {
                "domain": request.META["HTTP_HOST"],
                "cart_items_count":cart_items,
            }
    else:
        return {
            "domain": request.META["HTTP_HOST"],
        }
