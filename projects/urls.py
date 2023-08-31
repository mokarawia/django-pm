from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name = 'Project_List'),
    path('project/create', views.ProjectCreateView.as_view(), name = 'Project_Create'),
    path('project/update/<int:pk>', views.ProjectUpdateView.as_view(), name = 'Project_Update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name = 'Project_Delete'),
    path('task/create', views.TaskCreateView.as_view(), name = 'Task_Create'),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name = 'Task_Update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name = 'Task_Delete'),
]