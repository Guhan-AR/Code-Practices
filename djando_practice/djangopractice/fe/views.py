from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("This fe is working")
    return render(request,'example.html')

def frontend(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')