from django import forms
from django.contrib.auth.models import User
from .models import Employee, LeaveRequest

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'department', 'position', 'hire_date', 'salary', 'phone_number', 'address']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'reason', 'status', 'days_requested', 'admin_comment']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
            'admin_comment': forms.Textarea(attrs={'rows': 3}),
        }