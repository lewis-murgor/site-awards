from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length =100)
    project_image = models.ImageField(upload_to = 'images/')
    description = HTMLField()
    link = models.URLField(max_length =200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def search_by_title(cls,title):
        project = cls.objects.filter(title__icontains=title)
        return project

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.EmailField()
    
