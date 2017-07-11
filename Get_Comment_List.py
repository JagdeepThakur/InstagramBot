import requests

from token import BASE_URL,APP_ACCESS_TOKEN

from Get_Post_Id import get_post_id

from colorama import *

def get_like_list(insta_username) :

    media_id=get_post_id(insta_username)   #getting media id
    request_url=BASE_URL+"media/%s/likes?access_token=%s"%(media_id,APP_ACCESS_TOKEN)
    print "Get request URL:%s"%(request_url)
    user_media=requests.get(request_url).json()
    print user_media

    if user_media['meta']['code']==200 :
        print Fore.BLACK+Style.BRIGHT+"Media with media id {} is liked by following users:".format(media_id)
        for (index,user_likes) in enumerate(user_media['data']) :
            print "{}. {} ({})  -{}".format(index+1,user_likes['full_name'],user_likes['id'],user_likes['username'])
    else :
        print Fore.RED+Style.BRIGHT+"STATUS CODE OTHER THAN 200 RECIEVED"
