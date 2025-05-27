from django.contrib import admin
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
    
    path('admin/', admin.site.urls),
]
