from django.db import models
from admins.models import Admin

# Create your models here.
class EditedCommandsDB(models.Model):
    json = models.JSONField()
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    sender = models.ManyToManyField(Admin, related_name='sender', blank=True)
    
    def as_dict(self):
        return dict(
            id=self.pk, json=self.json, nickname=self.nickname,
            server=self.server, 
            time_created=self.time_created.isoformat(),
            sender=self.sender)