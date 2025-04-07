from django.forms import ModelForm
from .models import *

class Book_Form(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
