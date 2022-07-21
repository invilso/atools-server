from django.db import models

# Create your models here.
class Admin(models.Model):
    nickname = models.CharField(max_length=150, unique=True)
    online = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)