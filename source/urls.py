from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import search_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path("dashboard/", include("products.urls")),
    path("search/", search_view, name="q")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
