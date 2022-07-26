from typing import TypedDict
from .db import get_timedelta_warnings, get_all_warnings
from .longpoll import get_admin_server_from_nickname

class RequestData(TypedDict):
    nickname: str
    timedelta: int

def get_warnings_from_server(data: RequestData):
    server = get_admin_server_from_nickname(nickname=data['nickname'])
    if server:
        if data['timedelta'] > 0:
            qs = get_timedelta_warnings(data['timedelta']).filter(server=server)
        else:
            qs = get_all_warnings().filter(server=server)
        return qs.only('json', 'nickname', 'sender', 'time_created')
    
    