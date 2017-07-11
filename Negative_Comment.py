import requests

from textblob import TextBlob

#For Sentiment Analysis in Python, we use the libaray TextBlob

from textblob.sentiments import NaiveBayesAnalyzer

#NaiveBayesAnalyzer is same as Bays theorem in probability

#classifier for sentiment analysis.It uses the the data set of TextBlob library:

from token import BASE_URL,APP_ACCESS_TOKEN

from Get_Post_Id import get_post_id

from colorama import *


positive_comments=[]    #list to store list of positive comments

negative_comments=[]    #list to store number of negative comments


total_comments=[]       #list to store total number of comments

#this method is used for analysing The comment whether it is positive comment or negative comment


#Also deleting the comments from the user's posts if it is negative

def delete_negative_comment(insta_username):

    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:

        if len(comment_info['data']):

            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                total_comments.append(comment_text)  #adding total number of comments to the list
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())

                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    negative_comments.append(comment_text)  # adding negative comments
                    print Fore.RED+Style.BRIGHT+'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    positive_comments.append(comment_text)  #adding positive comments
                    print Fore.BLUE+Style.BRIGHT+'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'