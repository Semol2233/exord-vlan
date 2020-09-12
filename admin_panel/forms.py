from django import forms
from .models import Category

class Cetagory_form(forms.ModelForm): #Its Cetagory Forms.
    class Meta():
        model = Category
        fields = [
            'cetagory_name'
        ]
        widgets = {
            'cetagory_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Company Name...'}),     
        }

