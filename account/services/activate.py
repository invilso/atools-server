import json
import os
from time import sleep as wait
from account.models import User
from django.core.exceptions import ObjectDoesNotExist
from pathlib import Path


def get_data() -> list:
    my_file = Path("to_activate.json")
    if not my_file.exists():
        return save_data([])
  
    with open('to_activate.json', 'r', encoding='utf-8') as f:
        return json.loads(f.read())
    
def save_data(data):
    with open('to_activate.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(data))
        return data
    
    

def longpoll_get_new_admin(user: User) -> list[str]:
    for i in range(60):
        unactivated_users = get_data()
        if len(unactivated_users) > 0:
            unactivated_users_filtered = []
            for ua_user in unactivated_users:
                if not (user.username in ua_user['sended']):
                    unactivated_users_filtered.append(ua_user['username'])
                    ua_user['sended'].append(user.username)
            return unactivated_users_filtered
        wait(1)
    return False

def add_user_to_file(username: str):
    users = get_data()
    users.append({'username': username, 'sended': []})
    save_data(users)
    return True

def remove_user_from_file(username: str):
    users = get_data()
    for k, user in enumerate(users):
        if user['username'] == username:   
            users.pop(k)
            save_data(users)
            return True

def activate_user(username: str):
    try:
        user = User.objects.get(username=username, is_active=False)
        user.save()
        remove_user_from_file(username)
        return True
    except ObjectDoesNotExist:
        return False
    
def block_user(username: str):
    try:
        user = User.objects.get(username=username, is_active=False)
        user.delete()
        remove_user_from_file(username)
        return True
    except ObjectDoesNotExist:
        return False