import requests

from Get_User_Id import get_user_id

from common import BASE_URL,APP_ACCESS_TOKEN

import sys

from colorama import *

init()

# Function for getting post id of a particular post

def get_post_id(insta_username):

    sys.stdout.write(Fore.BLUE)

    user_id = get_user_id(insta_username)

    # If User Doesn't exists than server return none

    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

    print 'GET request url : %s' % (request_url)

    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
            print (Style.RESET_ALL)
    else:
        print 'Status code other than 200 received!'
        print (Style.RESET_ALL)
        exit()