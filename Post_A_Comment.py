import requests
from common import BASE_URL,APP_ACCESS_TOKEN
from Get_Post_Id import get_post_id

#insta_username="vishavgupta97"

#function for posting a comment to a particular post which belongs to certain user

def post_a_comment(insta_username) :
    media_id=get_post_id(insta_username)
    comment_text=raw_input("Kindly Enter Your Comment:\n")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    #sending data to the server and using payload

    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()
    if make_comment['meta']['code']==200 :
        print "Successfully Added New Comment"
    else :
        print "!!!Unable To add comment!!!Please try Again"
