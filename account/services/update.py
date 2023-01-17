from ..models import User
from django.utils import timezone
    
def update_spectate(user: User, spectate: int):
    if type(spectate) == int or spectate is None:
        user.spectate = spectate
        user.save()
        return True
    return False
        
def update_online(user: User):
    user.last_online = timezone.now()
    user.save()
    return True