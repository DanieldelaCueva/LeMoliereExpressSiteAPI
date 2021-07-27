from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=264)
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img_url = models.TextField()
    content = models.TextField()
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

