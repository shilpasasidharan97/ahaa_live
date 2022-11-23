from django.shortcuts import redirect


def auth_resturant(func):
    def wrap(request, *args, **kwargs):
        resturant_ex = request.user.restaurant
        if resturant_ex != None:
            return func(request, *args, **kwargs)
        else:
            return redirect("official:loginPage")
    return wrap