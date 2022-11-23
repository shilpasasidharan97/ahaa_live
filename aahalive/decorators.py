from django.shortcuts import redirect


def auth_resturant(func):
    def wrap(request, *args, **kwargs):
        franchise_ex = request.user.restaurant
        if franchise_ex != None:
            return func(request, *args, **kwargs)
        else:
            print('else')
            return redirect("official:loginPage")
    return wrap