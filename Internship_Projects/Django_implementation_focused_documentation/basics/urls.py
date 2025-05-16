from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='homepage'),
    path('',views.redirection),
    path('basics/',views.basics,name='basics'),
]