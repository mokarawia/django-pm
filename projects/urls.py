from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name = 'Project_List'),
    path('project/create', views.ProjectCreateView.as_view(), name = 'Project_Create'),
]