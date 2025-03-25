from django.forms import ModelForm
from .models import *

class Book_Form(ModelForm):

    class Meta:

        model = Book
        fields = "__all__"