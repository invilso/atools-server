from typing import TypedDict
from warnings_.services.longpoll import get_admin_server_from_nickname
from .db import create_admin, update_spectate, update_online


class RequestData(TypedDict):
    nickname: str
    spectate: int | None
    server: str | None
    
    
def update(data: RequestData, field: str):
    server = get_admin_server_from_nickname(data['nickname'])
    if server:
        if field == 'spectate':
            update_spectate(data['nickname'], data.get('spectate', None))
        elif field == 'online':
            update_online(data['nickname'])
    else:
        create_admin(server=data['server'], nickname=data['nickname'])