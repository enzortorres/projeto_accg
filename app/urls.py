from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('adotar/', views.adotar, name='adotar'),
    path('doacao/', views.doacao, name='doacao'),
    path('animais/', views.animais, name='animais'),
    path('animais/<int:animal_id>', views.animal, name='animal'),
    path('sobre/', views.sobre, name='sobre'),
    path('comoajudar/', views.como_ajudar, name='comoajudar'),
    path('apadrinhamento/', views.apadrinhamento, name='apadrinhamento'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)