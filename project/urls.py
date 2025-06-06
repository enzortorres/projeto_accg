from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]

# ! Para possibilitar adicionar várias fotos por animal, se fosse uma foto por animal, não seria necessário
if settings.DEBUG: # Isso somente se estiver em servidor de desenvolvimento (DEBUG = True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)