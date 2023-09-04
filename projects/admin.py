from django.contrib import admin
from django.db.models import Count
from . import models


admin.site.register(models.Category)


@admin.register(models.Project)
#To add the columns of Project in admin panel
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 20
    list_editable = ['status'] #Can be edited in admin panel
    list_select_related = ['category', 'user'] #This reduces number of queries while applying the code

    #tasks_count is new and is not found in database so we need to create it
    def tasks_count(self, obj):
        return obj.tasks_count

    #This reduces number of queries while applying the code
    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20