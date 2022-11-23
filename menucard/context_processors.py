from website.models import User,CartItems

def main_context(request):
    if request.session.exists(request.session.session_key):
        cart_items = CartItems.objects.filter(cart__cart_id = request.session.session_key).count()
        return {
            "domain": request.META["HTTP_HOST"],
            "cart_items_count":cart_items,
        }
    else:
        return {
            "domain": request.META["HTTP_HOST"],
        }