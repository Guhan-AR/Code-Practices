from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    task = models.Task.objects.all()
    if task:
        print('*'*20)
        print(task)
        print('*'*20)
    else:
        print('*'*20)
        print("nothing")
        print('*'*20)
    return HttpResponse("Please refresh")