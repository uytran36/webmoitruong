from django.urls import path
from . import views

urlpatterns = [
  #path('fontion1/', views.classification)
  path('', views.fonction2, name='fonction2'),
  path('result1', views.result1, name='result1')
]
