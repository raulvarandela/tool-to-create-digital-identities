from urllib import response
import requests
import json
from mastodon import Mastodon

'''response = requests.get("https://mstdn.social/api/v1/timelines/tag/cats?limit=2")
statuses = json.loads(response.text) # this converts the json to a python list of dictionary
assert statuses[0]["visibility"] == "public" # we are reading a public timeline
print(statuses[0]["content"]) # this prints the status text'''


# toot something using a created app

mastodon = Mastodon(
    access_token = 'jkunTgpxqP2sHunmjbltI_vBTx3MWIyYyjkFiRWHJ-E',
    api_base_url = 'https://mstdn.social/'
)
mastodon.toot('Tooting from python using #mastodonpy !')
print("Done!")


#create a new app

'''response = requests.post("https://mstdn.social/api/v1/apps?client_name=test2&redirect_uris=urn:ietf:wg:oauth:2.0:oob&scopes=read write follow push")
statuses = json.loads(response.text)
print(statuses)

mastodon2 = Mastodon(
    access_token = 'statuses[6]["vapid_key"]',
    api_base_url = 'https://mstdn.social/'
)

mastodon2.toot('Tooting from python using #mastodonpy !')'''