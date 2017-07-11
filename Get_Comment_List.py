import requests

from common import BASE_URL,APP_ACCESS_TOKEN

from Get_Post_Id import get_post_id

from colorama import init,Fore

init()

#this method is used to get comment lists of all the users who have commented to a particular post

def get_comment_list(insta_username) :

    media_id=get_post_id(insta_username)
    request_url=BASE_URL+"media/%s/comments/?access_token=%s"%(media_id,APP_ACCESS_TOKEN)
    print "Get Requested URL:%s"%(request_url)
    comment_info=requests.get(request_url).json()

    if comment_info['meta']['code']==200 :
        if len(comment_info['data']) :
            for x in range(0,len(comment_info['data'])) :
                comment_id=comment_info['data'][x]['id']
                comment_text=comment_info['data'][x]['text']
                print Fore.BLUE+Style.BRIGHT+"Comments are %s"%(comment_text)
        else:
            print "there is no comment regarding this post"
    else :
        print "status code other than 200 found"