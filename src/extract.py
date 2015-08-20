import requests
import json
import sys
from pprint import pprint

access_token='<put your access token here>'
page_id='<put your page id here>'


url='https://graph.facebook.com/v2.0/'+page_id+'?feed&access_token='+access_token
r = requests.get(url)

try:
	response_json = json.loads(r.text)
except (ValueError, KeyError, TypeError):
	print("JSON error")

pprint(response_json)
