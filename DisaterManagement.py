# This function will check if there is a natural calamity at a particular geographical coordinates

import requests

from common import BASE_URL,APP_ACCESS_TOKEN


#insta_username="jagdeep_thakur7"

def Location():


    # Getting location info according to geographical coordinates

    request_url = (BASE_URL + 'locations/search?lat=48.858844&lng=2.294351&access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    location_info = requests.get(request_url).json()

    # Getting recent media at a particular location

    request_url = (BASE_URL + 'locations/'+location_info['data']['id']+'/media/recent?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    caption_info = requests.get(request_url).json()

    if caption_info['meta']['code'] == 200:

        if len(caption_info['data']):

            for y in range(0, len(caption_info['data'])):

                caption_text = caption_info['data'][y]['caption']['text']
                caption = caption_text.split(" ")
                if 'earthquake' in caption or 'EARTHQUAKE' in caption:

                    print 'Read Caption: %s' % (caption)
                    print "Eathquake at %s" % (location_info['data']['name'])

                elif 'FLOODS' in caption or 'floods' in caption:

                        print 'Read Caption: %s' % (caption)
                        print 'Floods in %s' % (location_info['data']['name'])

                elif 'tornado' in caption or 'TORNADO' in caption:

                    print 'Read Caption: %s' % (caption)
                    print "Tornado in %s" % (location_info['data']['name'])

                elif 'landslides' in caption or 'LANDSLIDES' in caption:

                    print 'Read Caption: %s' % (caption)
                    print 'Landslides at %s' % (location_info['data']['name'])
                else:
                    print 'There are no natural calamity at given geographical coordinates!'

        else:

            print 'Status code other than 200 received!'
