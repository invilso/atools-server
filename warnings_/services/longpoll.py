from dataclasses import dataclass
import json
import admins
from admins.models import Admin
from time import sleep as wait
from .db import get_timedelta_warnings
from django.db.models import Q
from django.core import serializers
from django.forms.models import model_to_dict

@dataclass
class RequestData:
    nickname: str
    
def get_admin_from_nickname(nickname: str):
    try:
        return Admin.objects.get(nickname=nickname)
    except Admin.DoesNotExist:
        return False

def get_admin_server_from_nickname(nickname: str) -> str:
    a = get_admin_from_nickname(nickname=nickname)
    if a:
        return a.server

def longpoll(data: RequestData):
    admin_server = get_admin_server_from_nickname(nickname=data['nickname'])
    if admin_server:
        for i in range(60):
            qs = get_timedelta_warnings(minutes=5).filter(server=admin_server).filter(~Q(sended_to__nickname=data['nickname']))
            if len(qs) > 0:
                w = qs[0]
                w.sended_to.add(get_admin_from_nickname(nickname=data['nickname']))
                return w.as_dict()
            wait(1)
    return False