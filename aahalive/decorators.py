from django.shortcuts import redirect


def auth_restaurant(func):
    def wrap(request, *args, **kwargs):
        user = request.user
        try:
            if user is not None:
                if user.restaurant:
                    return func(request, *args, **kwargs)
                else:
                    return redirect("official:loginPage")
            else:
                return redirect("official:loginPage")
        except:
            return redirect("official:loginPage")

    return wrap


def auth_official(func):
    def wrap(request, *args, **kwargs):
        restaurant_ex = request.user
        if restaurant_ex is not None:
            if restaurant_ex.is_superuser:
                return func(request, *args, **kwargs)
            else:
                return redirect("official:loginPage")
        else:
            return redirect("official:loginPage")

    return wrap
