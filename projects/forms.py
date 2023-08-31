from django import forms
from . import models

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category']
        widgets = {
            'title' : forms.TextInput(),
            'description' : forms.Textarea(),
            'category' : forms.Select(),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'status', 'category']
        widgets = {
            'title' : forms.TextInput(),
            'status' : forms.Select(),
            'category' : forms.Select(),
        }