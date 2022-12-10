from . import views
from django.urls import path


app_name = "official"

urlpatterns = [
    path("login-page", views.loginPage, name="loginPage"),
    path("logout-resto", views.logout_resto, name="logout_resto"),
    path("", views.home, name="home"),
    path("resturant_list", views.resturantList, name="resturant_list"),
    path("resturant_details/<int:id>", views.resturantDetails, name="resturant_details"),
    path("create_user", views.creatUsers, name="create_user"),
    path("banneradding", views.bannerPage, name="banneradding"),
    path("product-banner", views.productBanner, name="productbanner"),
    path("video", views.videoAdding, name="video"),
]
