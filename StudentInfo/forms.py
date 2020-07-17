from django import forms
from django.forms import ModelForm
from .models import StudentInfo

class StudentAddForm(forms.ModelForm):
     # title = forms.CharField()
     # description = forms.CharField()
    class Meta:
        model = StudentInfo
        fields = ['title', 'description', 'author','category','image']


