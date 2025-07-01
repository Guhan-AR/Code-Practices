from django.urls import path , include

import login_reg.leave_page
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('leave/', login_reg.leave_page.leave_page, name='leave'),
    path('attendance/',include('attendance.urls'), name='attendance'),
    path('leaves/', views.leave_list_view, name='leave_view_list'),
]