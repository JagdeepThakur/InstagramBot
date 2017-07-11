import requests

from Get_Post_Id import get_post_id

from common import BASE_URL,APP_ACCESS_TOKEN

from colorama import *

#insta_username="jagdeep_thakur7"

#this method is used for liking a particular post


def like_a_post(insta_username) :

    media_id=get_post_id(insta_username)

    request_url=BASE_URL+"media/%s/likes"%(media_id)

    payload = {"access_token": APP_ACCESS_TOKEN}

    print "\nPost Request URL:%s"%(request_url)

    post_a_like = requests.post(request_url, payload).json()

    if post_a_like['meta']['code']==200 :
        print Fore.BLUE+Style.BRIGHT+"\nLike Was Successful"
        print(Style.RESET_ALL)
    else :
        print Fore.RED+"\nLike Was Not Successful!!!Kindly Try Again"
