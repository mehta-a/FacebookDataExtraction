import requests
import json
import sys
from pprint import pprint

access_token='CAACEdEose0cBAFRViNEjzSslz1ev8E84LSPZApBs2JiAbk7Tx5gmZCuMBIw7ZCFU1dd6ewa7ZAl4u5Y9nnEISGdCcYsI1ynXSIb9o7h9mhILZBzH86hUBJCFuzGQ2UrhfID0heqRHimD4aCcUm7hecfLeQIXZAOMN0qBFZCNvCMoLus2wBhI9RaBTMnOZBOPZCLWUiNWBMlFNW87VGop0KZChP'
page_id='CERCatIIITD'


url='https://graph.facebook.com/v2.0/'+page_id+'?feed&access_token='+access_token
r = requests.get(url)

try:
	response_json = json.loads(r.text)
except (ValueError, KeyError, TypeError):
	print("JSON error")

pprint(response_json)
