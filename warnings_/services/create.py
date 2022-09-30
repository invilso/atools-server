from http import server
from warnings_.models import Warning
from dataclasses import dataclass
from datetime import datetime, timedelta
import json
from .db import is_warning_exist_in_db


@dataclass
class RequestData:
    json: str
    sender: str
    server: str

def create_warning(data: RequestData):
    return True
    nickname = json.loads(data['json'])['origin_name']
    if not is_warning_exist_in_db(nickname):
        w = Warning(json=data['json'], nickname=nickname, sender=data['sender'], server=data['server'])
        w.save()
        return True
    return False