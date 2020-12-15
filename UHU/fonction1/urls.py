from django.urls import path
from . import views

urlpatterns = [
  #path('fontion1/', views.classification)
  path('', views.fonction1, name='fonction1'),
  path('result', views.result, name='result'),
  path('plus', views.plus, name='plus')
]
