import requests

from common import BASE_URL,APP_ACCESS_TOKEN

from Get_User_Id import get_user_id

service = ['natural' ,'earthquake' ,'flood' ,'weather' ,'trees' ,'thunderstorm' ,'hurricane' ,'drought' ,'environment' ,'birds' ,'landslide'
           ,'tornado' ,'tsunami' ,'blizzard']

#insta_username="jagdeep_thakur7"

def Location(insta_username):

    user_id = get_user_id(insta_username)
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s" % (user_id, APP_ACCESS_TOKEN))
    print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    user_info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            for post in range(0, len(user_info['data'])):
                pic_no = post + 1
                for temp in service:
                    if user_info['data'][post]['caption'] == None:
                        print("Sorry there is no hashtag inside the image...")

                    elif temp in user_info['data'][post]['caption']['text']:
                        print(user_info['data'][post]['caption']['text'])
                        pic_id = user_info['data'][post]['id']
                        comment_text = raw_input("Your comment: ")
                        payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                        request_url = (BASE_URL + 'media/%s/comments') % (pic_id)
                        print 'POST request url : %s' % (request_url)

                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully added a new comment!"
                        else:
                            print "Unable to add comment. Try again!"
                    else:
                        print("Sorry hashtag didn't match.Go further...")
            print("End of images...")
    else:
        print"Request failed."
