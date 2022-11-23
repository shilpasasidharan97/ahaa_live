from website.models import User

def main_context(request):
    if request.session.exists(request.session.session_key):
        resturant = request.user.restaurant
        if User.objects.filter(restaurant=resturant).exists():
            restaurant = request.user.restaurant
            return {
                "domain": request.META["HTTP_HOST"],
                "restaurant":restaurant,
            }
        else:
            return {
                "domain": request.META["HTTP_HOST"],
            }
    else:
        return {
            "domain": request.META["HTTP_HOST"],
        }