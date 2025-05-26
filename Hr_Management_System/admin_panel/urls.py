# admin_panel/urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Dashboard
    path('', login_required(views.AdminDashboardView.as_view()), name='admin_dashboard'),
    
    # Employee Management
    path('employees/', login_required(views.EmployeeListView.as_view()), name='employee_list'),
    path('employees/add/', login_required(views.EmployeeCreateView.as_view()), name='employee_create'),
    path('employees/<int:pk>/', login_required(views.EmployeeDetailView.as_view()), name='employee_detail'),
    path('employees/<int:pk>/edit/', login_required(views.EmployeeUpdateView.as_view()), name='employee_update'),
    path('employees/<int:pk>/delete/', login_required(views.EmployeeDeleteView.as_view()), name='employee_delete'),
    
    # Leave Management
    path('leaves/', login_required(views.LeaveRequestListView.as_view()), name='leave_list'),
    path('leaves/<int:pk>/', login_required(views.LeaveRequestDetailView.as_view()), name='leave_detail'),
    path('leaves/<int:pk>/edit/', login_required(views.LeaveRequestUpdateView.as_view()), name='leave_update'),
    path('leaves/<int:pk>/delete/', login_required(views.LeaveRequestDeleteView.as_view()), name='leave_delete'),
    path('leaves/<int:pk>/approve/', login_required(views.LeaveRequestApproveView.as_view()), name='leave_approve'),
    path('leaves/<int:pk>/reject/', login_required(views.LeaveRequestRejectView.as_view()), name='leave_reject'),
    
    # Profile
    path('profile/', login_required(views.AdminProfileView.as_view()), name='admin_profile'),
    path('profile/change-password/', login_required(views.ChangePasswordView.as_view()), name='admin_change_password'),

    path('mailing/',login_required(views.mailing),name='mailing')
]