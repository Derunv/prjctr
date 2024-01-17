import requests
import random
from keys import key_giphy as key
'''Please create in the same directory file with name  keys.py and add this
def key_giphy():
    return 'your giphy key'
def key_telegram():
    return 'your telegram id'
    '''


GIPHY_URL = 'https://api.giphy.com/v1/gifs/search'
payload = {'api_key': '', 'q': '', 'limit': 1, 'offset': 1, 'rating': 'g', 'lang': 'en',
           'bundle': 'messaging_non_clips'}


def get_giphy_data(search_word: str) -> dict:
    payload['api_key'] = key()
    payload['offset'] = random.randint(1,1000)
    # if payload['api_key'] == '':
    #     print('No API key provided')
    #     api_key = input('Press Enter yours API key to continue. If you do not have an API - just press Enter')
    #     if api_key == '':
    #         payload['api_key'] = key()
    #     else:
    #         payload['api_key'] = api_key
    if search_word == '':
        payload['q'] = 'cat'
        print(f'You didn`t write any word. I will searching for {payload["q"]}.')
    else:
        payload['q'] = search_word
    raw_response = requests.get(GIPHY_URL, params=payload)
    return raw_response.json()


def get_url_from_data(data):
    for obj in data["data"]:
        if obj["type"] == "gif":
            # print(obj['url'])
            return obj['url']


# request_gif = get_giphy_data(input('Enter your Giphy search word'))
# get_url_from_data(request_gif)
