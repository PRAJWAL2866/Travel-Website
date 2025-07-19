from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from travel import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
          ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
