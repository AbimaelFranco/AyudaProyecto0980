from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mostrar_perfiles, name='home'),
]
