from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
from django.views.generic import TemplateView

handler404 = 'fastshoe.views.handler404'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path('profile/', include('profiles.urls')),


    # Had to use https://adamj.eu/tech/2020/02/10/robots-txt/ to
    # get my robots.txt readable by lighthouse
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain")
        ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
