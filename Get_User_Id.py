from common import BASE_URL,APP_ACCESS_TOKEN

import requests

import sys

from colorama import *

#method for getting user id of the user and method takes instagram username as an input

def get_user_id(insta_username) :

    sys.stdout.write(Fore.BLUE)

    request_url=BASE_URL+"users/search?q=%s&access_token=%s"%(insta_username,APP_ACCESS_TOKEN)

    print "GET REQUEST URL :%s"%(request_url)

    user_info=requests.get(request_url).json()

    if user_info['meta']['code']==200 :
        if len(user_info['data']) :
            return user_info['data'][0]['id']
        else :
            return None
    else :
        print "Status Code Other Than 200 Is Recieved\n"
        exit()