from . import views
from django.urls import path


app_name = "website"

urlpatterns = [path("", views.home, name="home"), path("registration", views.registration, name="registration")]
