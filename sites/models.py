from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

RATE_CHOICE = (
    (10,'10'),
    (9,'9'),
    (8,'8'),
    (7,'7'),
    (6,'6'),
    (5,'5'),
    (4,'4'),
    (3,'3'),
    (2,'2'),
    (1,'1'),
)

class Project(models.Model):
    title = models.CharField(max_length =100)
    project_image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
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

class Rate(models.Model):
    design = models.IntegerField(choices=RATE_CHOICE)
    usability = models.IntegerField(choices=RATE_CHOICE)
    content = models.IntegerField(choices=RATE_CHOICE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    def average_rating(self):
        rating = ((self.design + self.usability + self.content)/3)
        return rating


    
