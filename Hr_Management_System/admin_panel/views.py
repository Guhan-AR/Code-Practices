from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Employee, LeaveRequest
from .forms import EmployeeForm, LeaveRequestForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.detail import DetailView
from django.views import View

from django.core.mail import send_mail
from django.conf import settings

def mailing(request):
    subject = 'Greeting from HRMS'
    message = 'This is a test mail from the HR management system.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['arguhan55@gmail.com']

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return HttpResponse("Mail sent successfully.")


class AdminRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('access_denied')
        return super().dispatch(request, *args, **kwargs)

class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin_panel/dashboard.html'

class EmployeeListView(AdminRequiredMixin, ListView):
    model = Employee
    template_name = 'admin_panel/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(AdminRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'admin_panel/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(AdminRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'admin_panel/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(AdminRequiredMixin, DeleteView):
    model = Employee
    template_name = 'admin_panel/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

class LeaveRequestListView(AdminRequiredMixin, ListView):
    model = LeaveRequest
    template_name = 'admin_panel/leave_list.html'
    context_object_name = 'leaves'

class LeaveRequestUpdateView(AdminRequiredMixin, UpdateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'admin_panel/leave_form.html'
    success_url = reverse_lazy('leave_list')

class LeaveRequestDeleteView(AdminRequiredMixin, DeleteView):
    model = LeaveRequest
    template_name = 'admin_panel/leave_confirm_delete.html'
    success_url = reverse_lazy('leave_list')

class AdminProfileView(AdminRequiredMixin, TemplateView):
    template_name = 'admin_panel/profile.html'

class EmployeeDetailView(AdminRequiredMixin, DetailView):
    model = Employee
    template_name = 'admin_panel/employee_detail.html'
    context_object_name = 'employee'

class LeaveRequestDetailView(AdminRequiredMixin, DetailView):
    model = LeaveRequest
    template_name = 'admin_panel/leave_detail.html'
    context_object_name = 'leave'

class LeaveRequestApproveView(AdminRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        leave = LeaveRequest.objects.get(pk=pk)
        leave.status = 'A'
        leave.save()
        messages.success(request, "Leave request approved.")
        return HttpResponseRedirect(reverse('leave_list'))

class LeaveRequestRejectView(AdminRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        leave = LeaveRequest.objects.get(pk=pk)
        leave.status = 'R'
        leave.save()
        messages.warning(request, "Leave request rejected.")
        return HttpResponseRedirect(reverse('leave_list'))

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'admin_panel/change_password.html'
    success_url = reverse_lazy('admin_profile')

    def form_valid(self, form):
        messages.success(self.request, "Your password was changed successfully.")
        return super().form_valid(form)