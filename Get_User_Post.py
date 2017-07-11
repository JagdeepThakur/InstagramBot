from token import BASE_URL,APP_ACCESS_TOKEN

from Get_User_Id import get_user_id

import urllib

#FOR DOWNLOADING ANY MEDIA FROM WORLD WIDE WEB

import requests
from colorama import *
from PIL import Image

def get_users_post(insta_username) :

    user_id=get_user_id(insta_username)

    if user_id==None :

        print Fore.RED+"Oooop!!!!!!User Doesn't Exists!!!!!"
        exit()

    request_url=BASE_URL+"users/%s/media/recent/?access_token=%s"%(user_id,APP_ACCESS_TOKEN)

    print "Get Request URL:%s"%(request_url)
    user_media=requests.get(request_url).json()

    if user_media['meta']['code']==200 :

        if len(user_media['data']) :
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print Fore.BLUE+Style.BRIGHT+"Users Post Is Successfully Downloaded"
            image = "C:\Users\gupta\PycharmProjects\instabot\\"+image_name
            img = Image.open(image)
            img.show()
            return user_media['data'][0]['id']

        else :
            print "THERE IS NOT ANY RECENT POSTS"

    else :
        print "Status Code Other Than 200 Is Recieved"
    return None