from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Article(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=264)
    date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=264, default="User")
    group = models.CharField(max_length=264, default="Collaborations externes")
    img_url = models.TextField()
    content = models.TextField()
    language = models.CharField(max_length=264, default="Français")
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Edition(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=264)
    date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title
    

