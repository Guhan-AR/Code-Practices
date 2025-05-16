from django import forms
from django.forms import ModelForm
from . import models

class VenueForm(ModelForm):
    class Meta:
        model = models.Venue_DB
        fields = ['name','address','pin_code','phone','web','email_address','venue_image']
        labels = {
            'name':'',
            'address':'',
            'pin_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
            'venue_image':'',
        }
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Name of the turf*'}),
            'address':forms.TextInput(attrs = {'class':'form-control','placeholder':'location of the turf*'}),
            'pin_code':forms.TextInput(attrs = {'class':'form-control','placeholder':'pin_code of location'}),
            'phone':forms.TextInput(attrs = {'class':'form-control','placeholder':'contact number'}),
            'web':forms.TextInput(attrs = {'class':'form-control','placeholder':'link'}),
            'email_address':forms.EmailInput(attrs = {'class':'form-control','placeholder':'mail id'}),
            'venue_image':forms.ClearableFileInput(attrs = {'class':'form-control','placeholder':'image'}),
        }

# Admin Event Form 
class EventFormAdmin(ModelForm):
    class Meta:
        model = models.Event_DB
        fields = ['name','date','venue','manager','attendees','description','event_images']
        labels = {
            'name':'',
            'date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'manager':'Manager',
            'description':'',
            'attendees':'',
            'event_images':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Event'}),
            'date':forms.TextInput(attrs = {'class':'form-control','placeholder':'Date of event'}),
            'venue':forms.Select(attrs = {'class':'form-select','placeholder':'Add Venue'}),
            'manager':forms.Select(attrs = {'class':'form-select','placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'event_images':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Event Image'}),
        }

# Event form for normal users
class EventForm(ModelForm):
    class Meta:
        model = models.Event_DB
        fields = ['name','date','venue','attendees','description','event_images']
        labels = {
            'name':'',
            'date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'description':'',
            'attendees':'',
            'event_images':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Event'}),
            'date':forms.TextInput(attrs = {'class':'form-control','placeholder':'Date of event'}),
            'venue':forms.Select(attrs = {'class':'form-select','placeholder':'Add Venue'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'event_images':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Event Image'}),
        }