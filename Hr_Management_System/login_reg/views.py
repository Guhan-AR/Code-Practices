from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from admin_panel.models import LeaveRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
def leave_list_view(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'accounts/leave_list.html', {'leaves': leaves})
