#!/usr/bin/env python

import requests, json
from requests.auth import HTTPBasicAuth

base_url = "https://elliotwillis.us.cumulocity.com"
managedObject_url = "/inventory/managedObjects"
all_mappings_filter = "query=$filter=(type+eq+'d11r_mapping')"

url = base_url + managedObject_url + "?" + all_mappings_filter
headers = {'Accept': 'application/json'}

auth = HTTPBasicAuth('Elliot', '-7rEr-*2NHEAKQ.D')

resp = requests.request("GET", url, headers=headers, data='', auth=auth)
data = json.loads(resp.text)

for object in data['managedObjects']:
    print(json.dumps(object['d11r_mapping'], indent=4))

