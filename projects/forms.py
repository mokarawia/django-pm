from django import forms
from . import models

attrs = {'class': 'form-control'} #To design the form fields in appropriate way

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title' : forms.TextInput(attrs=attrs),
            'description' : forms.Textarea(attrs=attrs),
            'category' : forms.Select(attrs=attrs),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'status', 'category']
        widgets = {
            'title' : forms.TextInput(attrs=attrs),
            'status' : forms.Select(attrs=attrs),
            'category' : forms.Select(attrs=attrs),
        }