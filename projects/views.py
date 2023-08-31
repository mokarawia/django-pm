from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy, reverse

# Create your views here.

class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_List')

class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    
    #This will return the same page when submitting
    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.id]) #Here object refers to project

class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_List')
    
class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post'] #This will give error when trying to get the page task/create as we need to post the result only and not to get it


    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id]) #Here object refers to task so we need to specify id of project

class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post'] 


    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])  

class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])  