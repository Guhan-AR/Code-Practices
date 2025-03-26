from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page),
    path('admim',views.admini),
    path('search',views.search)
]