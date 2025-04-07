from django.urls import path
from . import views

urlpatterns=[
    path('book/',views.show_book),
    path('customer/',views.show_customer),
    path('book/delete/<int:id>',views.delete_book,name='deletes_book'),
    path('customer/delete/<int:id>',views.delete_customer,name="delete_customer"),
    path('customer/add_customer/',views.add_customer),
    path('book/update/<int:id>',views.update_book,name='update_book'),
    path('customer/update/<int:id>',views.update_customer,name='update_customer'),
    path('book/add_book/',views.add_book)
]