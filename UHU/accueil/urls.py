from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('propos/', views.propos, name='propos'),
]