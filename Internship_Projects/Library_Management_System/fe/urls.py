from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('<int:id>',views.delete_book,name='deletes_book'),
    path('add/',views.add_book)
]