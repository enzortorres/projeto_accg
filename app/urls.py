from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adotar/', views.adotar),
    path('admin/', admin.site.urls),
]
