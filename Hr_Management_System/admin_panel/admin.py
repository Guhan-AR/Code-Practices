from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Employee, LeaveRequest

# Extend UserAdmin to include Employee info
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employee Details'

class CustomUserAdmin(UserAdmin):
    inlines = (EmployeeInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_department', 'get_position')
    
    def get_department(self, obj):
        return obj.employee.department if hasattr(obj, 'employee') else None
    get_department.short_description = 'Department'
    
    def get_position(self, obj):
        return obj.employee.position if hasattr(obj, 'employee') else None
    get_position.short_description = 'Position'

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position', 'hire_date', 'is_active')
    list_filter = ('department', 'position', 'is_active')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'department')
    raw_id_fields = ('user',)

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status', 'days_requested')
    list_filter = ('status', 'leave_type', 'start_date')
    search_fields = ('employee__user__username', 'employee__user__first_name', 'employee__user__last_name')
    actions = ['approve_leave', 'reject_leave']
    
    def approve_leave(self, request, queryset):
        queryset.update(status='A')
    approve_leave.short_description = "Approve selected leave requests"
    
    def reject_leave(self, request, queryset):
        queryset.update(status='R')
    reject_leave.short_description = "Reject selected leave requests"