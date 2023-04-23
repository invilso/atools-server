from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=64, unique=True)
    server = models.CharField(max_length=64, blank=True, null=True)
    last_online = models.DateTimeField(blank=True, null=True)
    spectate = models.IntegerField(blank=True, null=True)
    social_network = models.CharField(max_length=64, blank=True, null=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.CharField(max_length=64)
#     server = models.CharField(max_length=32)
#     last_online = models.DateTimeField(blank=True, null=True)
#     spectate = models.IntegerField(blank=True, null=True)
#     def __str__(self) -> str:
#         return self.nickname


class Blocklist(models.Model):
    reason = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.reason} || {self.ip}'
    
class Ad(models.Model):
    text = models.TextField()
    link = models.URLField(blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
