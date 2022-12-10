from . import views
from django.urls import path


app_name = "website"

urlpatterns = [path("", views.websitehome, name="websitehome"), path("registration", views.registration, name="registration")]
