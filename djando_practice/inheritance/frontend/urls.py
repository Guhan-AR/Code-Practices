from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('Home',views.home),
    path('About',views.about),
    path('Contact',views.contact),
    path('Services',views.services),
]