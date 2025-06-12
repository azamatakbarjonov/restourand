from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('data/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('books/', include('booking.urls')),
    path('contact/', include('contact.urls')),
    path('service/', include('service.urls')),
    path('menu/', include('menu.urls')),
    path('chef/', include('chef.urls')),
    path('koment/', include('koment.urls')),
    path('base/', include('base.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



