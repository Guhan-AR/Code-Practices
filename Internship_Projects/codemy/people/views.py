from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import forms

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password = password)
        if user is not None:
            messages.success(request,('Logged In'))
            login(request,user)
            return redirect('calendar')
        else:
            messages.success(request,('Error Logging in...'))
            return redirect('log-in')
    else:
        context={}
        return render(request , 'authenticate/login.html' , context)


def logout_user(request):
    logout(request)
    messages.success(request,('You Were Logged Out'))
    return redirect('calendar')

def register_user(request):
    if request.method == 'POST':
        posted_form = forms.RegisterUserForm(request.POST)
        context = {'form':posted_form}
        if posted_form.is_valid():
            posted_form.save()
            username = posted_form.cleaned_data['username']
            password = posted_form.cleaned_data['password1']
            user = authenticate(request,username=username,password = password)
            login(request, user)
            messages.success(request,('Registration successfull!'))
            return redirect('calendar')
    else:
        posted_form = forms.RegisterUserForm(request.POST)
        context = {'form':posted_form}
    return render(request,'authenticate/register.html',context)