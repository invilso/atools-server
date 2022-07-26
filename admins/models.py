from django.db import models

# Create your models here.
class Admin(models.Model):
    nickname = models.CharField(max_length=150, unique=True)
    last_online = models.DateTimeField(blank=True, null=True)
    spectate = models.IntegerField(blank=True, null=True)
    server = models.CharField(max_length=32)
    time_created = models.DateTimeField(auto_now_add=True)