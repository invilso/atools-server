from django.db import models
from admins.models import Admin

# Create your models here.

class Warning(models.Model):
    json = models.TextField()
    nickname = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    sended_to = models.ManyToManyField(Admin)