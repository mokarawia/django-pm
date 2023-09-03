from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6 #This ensures that the page will show 6 projects only

    #To get the result of search bar
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user} #This will get the project list of current user only
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_List')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'

    #This will show the page only to the logged in user and can't be accessed by other users
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
    #This will return the same page when submitting
    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.id]) #Here object refers to project

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_List')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
class TaskCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post'] #This will give error when trying to get the page task/create as we need to post the result only and not to get it

    def test_func(self):
        project_id = self.request.POST.get('project', '') #project here is the project id named in task.html
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id]) #Here object refers to task so we need to specify id of project

class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post'] 

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])  

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_Update', args=[self.object.project.id])  