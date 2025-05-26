from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LeaveRequestForm
from django.contrib import messages
from admin_panel.models import LeaveRequest,Employee
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        else:
            return redirect('dashboard')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        
        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

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






@login_required(login_url='login')
def leave_list_view(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'accounts/leave_list.html', {'leaves': leaves})
