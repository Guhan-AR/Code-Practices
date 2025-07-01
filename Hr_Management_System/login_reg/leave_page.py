from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from admin_panel.models import Employee
from login_reg.forms import LeaveRequestForm


@login_required(login_url='login')
def leave_page(request):
    employee = Employee.objects.filter(user=request.user).first()

    if not employee:
        messages.error(request, "Only employees can apply for leave.")
        return redirect('dashboard')  # or any other page you want

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee  # link the employee properly
            leave.status = 'P'  # P = Pending
            leave.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('leave')
    else:
        form = LeaveRequestForm()

    return render(request, 'accounts/leave.html', {'form': form})
