from django.shortcuts import render, redirect
from .forms import *
from .models import *

def show_book(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'show_book.html',context)

def show_customer(request):
    return render(request,'show_customer.html',{'customers':Customer.objects.all()})

def add_book(request):
    context = {'book_form': Book_Form()}
    if request.method == 'POST':
        book_form = Book_Form(request.POST , request.FILES)
        if book_form.is_valid():
            book_form.save()
    return render(request, 'adding_books.html', context)

def delete_book(request,id):
    selected_book = Book.objects.get(id=id)
    selected_book.delete()
    return redirect('/')

def update_book(request,id):
    selected_book = Book.objects.get(id = id)
    if request.method == "POST":
        book_form = Book_Form(request.POST,request.FILES,instance=selected_book)
        if book_form.is_valid():
            book_form.save()
    return render(request , "update_book.html" , {"book_form":Book_Form(instance=selected_book)})

def add_customer(request):
    context = {'add_customers':Customer_Form}
    if request.method == 'POST':
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
        else:
            print("problem of validation.","*"*20)
    return render(request,"add_customer.html",context)

def delete_customer(request,id):
    selected_customer = Customer.objects.get(id = id)
    selected_customer.delete()
    return redirect('/')

def update_customer(request,id):
    selected_customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = Customer_Form(request.POST,instance=selected_customer)
        if form.is_valid():
            form.save()
    return render(request, "update_customer.html",{"a":Customer_Form(instance=selected_customer)})