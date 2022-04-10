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
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_description(self, updated_description):
        self.description = updated_description
        self.save

    @classmethod
    def search_by_title(cls,title):
        project = cls.objects.filter(title__icontains=title)
        return project

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    contact = models.EmailField()

    def __str__(self):
        return self.Bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self, updated_profile):
        self.profile = updated_profile
        self.save()


    
