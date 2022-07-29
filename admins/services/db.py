from datetime import timedelta
from admins.models import Admin
from django.utils import timezone
from warnings_.services.longpoll import get_admin_from_nickname


def create_admin(nickname: str, server: str):
    a = Admin(nickname=nickname, server=server, last_online=timezone.now())
    a.save()
    return True
    
def update_spectate(nickname: str, spectate: int):
    a = get_admin_from_nickname(nickname=nickname)
    a.spectate = spectate
    a.save()
    return True
    

def update_online(nickname: str):
    a = get_admin_from_nickname(nickname=nickname)
    a.last_online = timezone.now()
    a.save()
    
def get_all_admins():
    return Admin.objects.all()
    
def get_timedelta_admins(minutes: int):
    time = timezone.now() - timedelta(minutes=minutes)
    return get_all_admins().filter(last_online__gte=time)
    