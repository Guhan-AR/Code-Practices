from django.shortcuts import render , redirect
from calendar import HTMLCalendar
from datetime import datetime
from . import models
from . import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def calendar(request, year = datetime.now().year, month =datetime.now().month, name='User'):

    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # setting month in number format
    if isinstance(month,int):
        month_number = month
    else:
        month= month.capitalize()
        month_number =month_list.index(month)+1
    
    # finding current date and time
    now = datetime.now()
    current_year = now.year

    # extracting html view of the calender
    cal = HTMLCalendar().formatmonth(year,month_number,True)

    context={'name':name,'cal':cal,'current_year':current_year,'month':month_list[month_number],'year':year}

    return render(request , 'events/greetings.html',context)

def all_events(request):

    event_list = models.Event_DB.objects.all()
    return render(request, 'events/event_list.html',{'event_list':event_list})

def list_venue(request):

    # venue_list = models.Venue_DB.objects.all().order_by('?')
    venue_list = models.Venue_DB.objects.all()

    # set up pagination
    p=Paginator(models.Venue_DB.objects.all(),3)
    page = request.GET.get('page')
    venue = p.get_page(page)

    context = {'venue_list':venue_list,'venue':venue}
    
    return render(request , 'events/list_venue.html',context)

def venue_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = models.Venue_DB.objects.filter(name__contains = searched)
        context = {'searched':searched,'venues':venues}
    else:
        context = {}
    return render(request , 'events/venue_search.html' , context)


def venue(request,venue_id):
    crt_venue = models.Venue_DB.objects.get(pk = venue_id)
    owner = User.objects.get(pk = crt_venue.owner)
    print('*'*20)
    print(owner)
    print('*'*20)
    context = {'venue':crt_venue,'owner':owner}
    return render(request , 'events/venue.html' , context)

def add_event(request):
    submitted = False

    if request.method == 'POST':
        
        if request.user.is_superuser:
            form = forms.EventFormAdmin(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = forms.EventForm(request.POST,request.FILES)
            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user
                event.save()
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        if request.user.is_superuser:
            form = forms.EventFormAdmin
        else:
            form = forms.EventForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'events/add_event.html', context)

def add_venue(request):
    submitted = False

    if request.method == 'POST':
        form = forms.VenueForm(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = forms.VenueForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form,'submitted':submitted}
    return render(request , 'events/add_venue.html',context)

def update_venue(request,venue_id):
    vdata = models.Venue_DB.objects.get(pk = venue_id)
    owner = User.objects.get(id = vdata.owner)
    if request.user == owner or request.user.is_superuser:
        form = forms.VenueForm(request.POST,request.FILES or None,instance=vdata)
        if form.is_valid():
            form.save()
            return redirect('list-venue')
        context = {'form':form}
        return render(request, 'events/update_venue.html',context)
    else:
        context = {}
        messages.success(request,("You aren't authorized to update"))
        return redirect('calendar')

def update_event(request, event_id):
    event_data = models.Event_DB.objects.get(id = event_id)
    if request.user.is_superuser:
        event = forms.EventFormAdmin((request.POST,request.FILES) or None,instance=event_data)
        if event.is_valid():
            event.save()
            return redirect('list-events')
    else:
        event = forms.EventForm((request.POST,request.FILES) or None,instance=event_data)
        if event.is_valid():
            event.save()
            messages.success(request, ('Updates Event Successfully'))
            return redirect('list-events')
    context = {'form':event}
    return render(request , 'events/update_events.html',context)

def delete_venue(request,id):
    selected_venue = models.Venue_DB.objects.get(id = id)

    owner = User.objects.get(pk = selected_venue.owner)

    if owner==request.user:
    
        selected_venue.delete()
    
    else:

        messages.error('ure not authorized')
    return redirect('list-venue')

def delete_event(request,id):
    data = models.Event_DB.objects.get(id = id)
    if request.user == data.manager:
        messages.success(request,('Deleted The event'))
        data.delete()
    else:
        messages.success(request,('Authorized user only delete it'))
    return redirect('list-events')