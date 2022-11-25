from website.models import RestoSave, User,CartItems

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



def main_context(request):
    if request.session.exists(request.session.session_key):
        cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
        resto = RestoSave.objects.get(user_session_id=request.session.session_key)
        return {
            "domain": request.META["HTTP_HOST"],
            "cart_items_count":cart_items,
            "resto":resto,
        }
    else:
        return {
            "domain": request.META["HTTP_HOST"],
        }




# def main_context(request):
#     if request.session.exists(request.session.session_key):
#         cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
#         try:
#             resto = RestoSave.objects.get(user_session_id=request.session.session_key)
#             return {
#                 "domain": request.META["HTTP_HOST"],
#                 "cart_items_count":cart_items,
#                 "resto":resto,
#             }
#         except :
#             return {
#                 "domain": request.META["HTTP_HOST"],
#                 "cart_items_count":cart_items,
#             }
#     else:
#         return {
#             "domain": request.META["HTTP_HOST"],
#         }
