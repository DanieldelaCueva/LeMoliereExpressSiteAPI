from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, to_field='username', primary_key=True, on_delete=models.CASCADE)

    group = models.ForeignKey(Group, to_field="name", default="Staff", on_delete=models.CASCADE)
    age_class = models.CharField(max_length=264)
    class Meta:
        verbose_name_plural = "User Data"
