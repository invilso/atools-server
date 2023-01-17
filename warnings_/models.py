from django.db import models
from admins.models import Admin

# Create your models here.

class Warning(models.Model):
    json = models.JSONField()
    nickname = models.CharField(max_length=150)
    sender = models.CharField(max_length=150)
    server = models.CharField(max_length=32)
    sended_all = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    sended_to = models.ManyToManyField(Admin, related_name='sended_to', blank=True)
    
    def __str__(self) -> str:
        return f'{self.pk} {self.nickname} {self.sender}'
    
    def as_dict(self):
        return dict(
            id=self.pk, json=self.json, nickname=self.nickname,
            server=self.server, 
            time_created=self.time_created.isoformat(),
            sender=self.sender)