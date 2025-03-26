from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q

def landing_page(request):
    context = {
        'add_product' : Product_db.objects.all()
    }
    return render(request,'landing_page.html',context)

def admini(request):

    context = {
        'add_product' : adding_product()
    }
    if request.method == 'POST':
        add_product = adding_product(request.POST,request.FILES)
        print('before if')
        if add_product.is_valid():
            print('*'*30)
            add_product.save()
        else:
            print(add_product)
    return render(request,'forms.html',context)

def search(request):
    if request.method == 'POST':
        print("yes data passing on post")
        searched = request.POST['searched']
        searcher = Product_db.objects.filter(Q(name__icontains=searched) | Q(price__icontains=searched))
        return render(request,'search.html',{'i':searched,'j':searcher})
    else:
        print("no data passing")
        return render(request,'search.html')