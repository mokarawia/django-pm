from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 255)
    
    def __str__(self):  
        return self.name #To return the name of the category
    
    #To translate Category in admin panel
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')

class ProjectStatus(models.IntegerChoices):
    PENDING = 1, 'Pending'
    COMPLETED = 2, 'Completed'
    POSTPONED = 3, 'Postponed'
    CANCELED = 4, 'Canceled'

    
class Project(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    status = models.IntegerField(
        choices = ProjectStatus.choices,
        default = ProjectStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT) #if the user is deleted, any related project won't be deleted
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE, null =True) #if the user is deleted, any related project will be deleted

    def __str__(self):  
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Project')

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default= False)
    project = models.ForeignKey(Project, on_delete= models.CASCADE)

    def __str__(self):  
        return self.description
    
    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Task')
    