from datetime import timedelta
from typing import TypedDict
from warnings_.services.longpoll import get_admin_server_from_nickname
from admins.services.db import get_timedelta_admins, get_all_admins


class RequestData(TypedDict):
    nickname: str
    timedelta: int

def get_admins_from_server(data: RequestData):
    server = get_admin_server_from_nickname(nickname=data['nickname'])
    if server:
        if data['timedelta'] > 0:
            qs = get_timedelta_admins(data['timedelta']).filter(server=server)
        else:
            qs = get_all_admins().filter(server=server)
        return qs.values('last_online', 'nickname', 'spectate', 'time_created')