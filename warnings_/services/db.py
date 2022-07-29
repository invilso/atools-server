from warnings_.models import Warning
from datetime import timedelta
from django.utils import timezone

def get_all_warnings():
    return Warning.objects.all()

def get_timedelta_warnings(minutes: int):
    time = timezone.now() - timedelta(minutes=minutes)
    return get_all_warnings().filter(time_created__gte=time)

def is_warning_exist_in_db(nickname: str):
    return get_timedelta_warnings(minutes=2).filter(nickname=nickname).exists()