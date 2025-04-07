from django import forms
from django.forms import ModelForm
from . import models

class VenueForm(ModelForm):
    class Meta:
        model = models.Venue_DB
        fields = "__all__"
        labels = {
            'name':'',
            'address':'',
            'pin_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
        }
        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Name of the turf*'}),
            'address':forms.TextInput(attrs = {'class':'form-control','placeholder':'location of the turf*'}),
            'pin_code':forms.TextInput(attrs = {'class':'form-control','placeholder':'pin_code of location'}),
            'phone':forms.TextInput(attrs = {'class':'form-control','placeholder':'contact number'}),
            'web':forms.TextInput(attrs = {'class':'form-control','placeholder':'link'}),
            'email_address':forms.EmailInput(attrs = {'class':'form-control','placeholder':'mail id'}),
        }