from django import forms
from .models import videomo,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = videomo
        fields = ['title','clip','photo']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
        }

class PostNews(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','body','photo']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'author':forms.Select(attrs={'class':'form-control'}),
        }
    def __init__(self,*args, **kwargs):
        super(PostNews,self).__init__(*args, **kwargs)
        self.fields['author'].empty_label="Select Author"


