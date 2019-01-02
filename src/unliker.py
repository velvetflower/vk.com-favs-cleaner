import vk_requests
import time
import re
import random
import requests
from requests.exceptions import Timeout

token = ""
api = vk_requests.create_api(service_token=token, scope=['friends', 'wall', 'offline'], interactive=True)

cntr = 0
gcntr = 0
getphotos = api.fave.getPhotos()
ofsete = 100
getposts = api.fave.getPosts(offset=ofsete)

def photos():
    global getphotos
    global getposts
    global cntr
    global gcntr
    while cntr != 49:
        try:
            item = getphotos['items'][cntr]['id']
            owner = getphotos['items'][cntr]['owner_id']
            hey = api.likes.delete(type='photo',owner_id=owner,item_id=item)
            print (hey,"#",cntr," -> ",gcntr)
            cntr += 1
            gcntr += 1
            time.sleep(random.randint(3,6))
            if cntr == 48:
                getphotos = api.fave.getPhotos()
                cntr = 0
        except Exception as e:
            getphotos = api.fave.getPhotos()
            cntr = 0
            print (e)
            time.sleep(random.randint(3,6))

def posts():
    global getphotos
    global getposts
    global cntr
    global gcntr
    while cntr != 49:
        try:
            item = getposts['items'][cntr]['id']
            owner = getposts['items'][cntr]['owner_id']
            hey = api.likes.delete(type='post',owner_id=owner,item_id=item)
            print (hey,"#",cntr," -> ",gcntr)
            cntr += 1
            gcntr += 1
            time.sleep(random.randint(3,6))
            if cntr == 48:
                getposts = api.fave.getPosts(offset=ofsete)
                cntr = 0
        except Exception as e:
            getposts = api.fave.getPosts(offset=ofsete)
            cntr = 0
            print (e)
            time.sleep(random.randint(3,6))

def start():
    choiceme = input('''
С чего снимаем лайки?:

1. Фото
2. Посты
выбор: ''')
    if choiceme == '1':
        photos()
    elif choiceme == '2':
        posts()
    else:
        start()

start()

        




        

