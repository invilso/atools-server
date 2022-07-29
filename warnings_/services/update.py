from typing import TypedDict

from warnings_.services.longpoll import get_admin_server_from_nickname
from .db import get_all_warnings

class RequestData(TypedDict):
    id: int
    nickname: str
    

def send_to_all(data: RequestData):
    server = get_admin_server_from_nickname(nickname=data['nickname'])
    if server:
        x = get_all_warnings().get(pk=data['id'])
        if x.sended_all == False:
            x.sended_all = True
            x.save()
            return True
        return False