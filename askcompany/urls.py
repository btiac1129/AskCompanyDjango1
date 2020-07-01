from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# settings.MEDIA_URL
# settings.MEDIA_ROOT
