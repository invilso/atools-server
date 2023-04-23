from django.contrib import admin
from .models import Blocklist, User, Ad


admin.site.register(User)  
admin.site.register(Blocklist)
admin.site.register(Ad)
