from django.forms import ModelForm
from .models import *

class adding_product(ModelForm):

    class Meta:

        model = Product_db
        fields = "__all__"