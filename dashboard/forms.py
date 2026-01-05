from .models import Child
from django import forms



class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name','date_of_birth' ]
        widgets = {
             "name": forms.TextInput(attrs={"class": "form-control"}),
             "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }