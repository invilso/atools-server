from django.contrib import admin
from .models import Blocklist, User


admin.site.register(User)  
admin.site.register(Blocklist)
