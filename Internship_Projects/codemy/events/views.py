from django.shortcuts import render , redirect
from calendar import HTMLCalendar
from datetime import datetime
from . import models
from . import forms
from django.http import HttpResponseRedirect


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

def add_venue(request):
    submitted = False

    if request.method == 'POST':
        form = forms.VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = forms.VenueForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form,'submitted':submitted}
    return render(request , 'events/add_venue.html',context)

def list_venue(request):

    venue_list = models.Venue_DB.objects.all()
    context = {'venue_list':venue_list}
    return render(request , 'events/list_venue.html',context)

def venue(request,venue_id):
    crt_venue = models.Venue_DB.objects.get(pk = venue_id)
    context = {'venue':crt_venue}
    return render(request , 'events/venue.html' , context)

def venue_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = models.Venue_DB.objects.filter(name__contains = searched)
        context = {'searched':searched,'venues':venues}
    else:
        context = {}
    return render(request , 'events/venue_search.html' , context)

def update_venue(request,venue_id):
    vdata = models.Venue_DB.objects.get(pk = venue_id)
    form = forms.VenueForm(request.POST or None,instance=vdata)
    if form.is_valid():
        form.save()
        return redirect('list-venue')
    context = {'form':form}
    return render(request, 'events/update_venue.html',context)
def delete_venue(request,id):
    selected_venue = models.Venue_DB.objects.get(id = id)
    selected_venue.delete()
    return redirect('list-venue')