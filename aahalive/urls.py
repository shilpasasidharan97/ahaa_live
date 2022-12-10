from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("menucard.urls")),
        path("", include("website.urls")),
        path("web/", include("web.urls")),
        path("official/", include("official.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
