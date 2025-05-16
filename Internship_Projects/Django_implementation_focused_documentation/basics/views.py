from django.shortcuts import render , redirect

# Create your views here.
def home(request):
    return render(request , 'home.html')

def redirection(request):
    return redirect('basics/home/')

def basics(request):
    return render(request , 'basic/basics.html')