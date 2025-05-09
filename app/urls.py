from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('adotar/', views.adotar, name='adotar'),
    path('apadrinhamento/', views.apadrinhamento, name='apadrinhamento'),
    path('admin/', admin.site.urls),
]
