from Get_User_Id import get_user_id

import requests

from common import BASE_URL,APP_ACCESS_TOKEN

from colorama import init,Fore,Style

init()


# Mehod FoR Getting information of a particular user

def get_user_info(insta_username) :

    user_id=get_user_id(insta_username)

    # If Nothing is recieved from server

    if user_id == None:
        print Fore.RED+"User does not exist!!"
        print (Style.RESET_ALL)
        exit()

    request_url=BASE_URL+"users/%s?access_token=%s"%(user_id,APP_ACCESS_TOKEN)
    print "GET REQUESTED URL:%s"%(request_url)
    user_info=requests.get(request_url).json()

    if user_info['meta']['code']==200 :
        if len(user_info['data']) :
            print Fore.BLUE+Style.BRIGHT+"Username Is : %s"%(user_info['data']['username'])
            print "There are Total %s Followers for This User"%(user_info['data']['counts']['followed_by'])
            print "No. Of posts are %s"%(user_info['data']['counts']['media'])
            print "Follows:%s"%(user_info['data']['counts']['follows'])
            print(Style.RESET_ALL)
        else :
            print Fore.RED+Style.BRIGHT+"THERE IS NO DATA FOR THIS USER"
            print(Style.RESET_ALL)
    else :
        print "Status Code Other Than 200 Is Recieved"