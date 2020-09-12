from django import forms
from django.contrib.auth.models import User
from .models import *

class Userform(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','password','email']
        widgets = {
          'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
          'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
          'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
        }

class profilepictures(forms.ModelForm):
    class Meta():
        model = profileinfo
        fields = ['photo']



class PostNews(forms.ModelForm):
    class Meta:
        model = Post_Asn
        fields = ['id','VLAN','LOCATION','DESCRIPTION']
        widgets = {
            'VLAN':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'LOCATION':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'DESCRIPTION':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Name...'})
          
        }
    # def __init__(self,*args, **kwargs):
    #     super(PostNews,self).__init__(*args, **kwargs)
    #     self.fields['author'].empty_label="Select Author"


class PostNewsup(forms.ModelForm):
    class Meta:
        model = Post_Asn
        fields = ['id','VLAN','LOCATION','DESCRIPTION']
        widgets = {
            'VLAN':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'LOCATION':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'DESCRIPTION':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Name...'})
          
        }
    # def __init__(self,*args, **kwargs):
    #     super(PostNews,self).__init__(*args, **kwargs)
    #     self.fields['author'].empty_label="Select Author"


