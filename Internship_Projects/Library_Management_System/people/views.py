from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.error(request, 'Logged in successfully')
            redirect('show_book')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login_user')
    else:
        return render(request , 'authenticate/login.html')