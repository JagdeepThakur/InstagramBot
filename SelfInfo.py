import requests

from common import BASE_URL,APP_ACCESS_TOKEN

from colorama import  *

# Mehod For Getting your own Information

def self_info() :

    requests_url=(BASE_URL)+"users/self/?access_token=%s"%(APP_ACCESS_TOKEN)

    print "Get Request URL:%s"%(requests_url)

    # Get mehod Is Used For Getting Own Information

    user_info=requests.get(requests_url).json()

    if user_info['meta']['code']==200 :

        if len(user_info['data']) :

            # Information of current user

            print Fore.GREEN+Style.BRIGHT+"\nUSERNAME: %s"%(user_info['data']['username'])
            print "\nYou have %s followers"%(user_info['data']['counts']['followed_by'])
            print "\nyou are following %s people" % (user_info['data']['counts']['follows'])
            print "\nYou Have %s No. of posts" % (user_info['data']['counts']['media'])
            print(Style.RESET_ALL)
        else :

            # This executes when nothing is recieved from the server

            print Fore.RED+Style.BRIGHT+"\nSorry!!!!This User Doesn't Exists"
            print(Style.RESET_ALL)
    else :
        print Fore.RED+Style.BRIGHT+"\n!!!Status Code Other Than 200 Recieved!!!"
        print(Style.RESET_ALL)


