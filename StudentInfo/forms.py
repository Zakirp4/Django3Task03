from django import forms
from django.forms import ModelForm
from .models import StudentInfo

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'roll', 's_class']


