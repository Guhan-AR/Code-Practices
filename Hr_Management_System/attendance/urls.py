from django.urls import path , include
from .views import attendance_view

urlpatterns = [
    path('', attendance_view, name='attendance'),
]