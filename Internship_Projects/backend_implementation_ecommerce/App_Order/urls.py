from django.urls import path

import App_Order.decrease_cart.decrease_cart
from App_Order import views

app_name = 'App_Order'

urlpatterns = [
    path('add/<pk>', views.add_to_cart, name='add'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<pk>', views.remove_from_cart, name='remove'),
    path('increase/<pk>/', views.increase_cart, name='increase'),
    path('decrease/<pk>/', App_Order.decrease_cart.decrease_cart.decrease_cart, name='decrease'),
]
