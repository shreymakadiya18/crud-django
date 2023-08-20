from django import forms
from .models import *

class CrudForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['name','phone']