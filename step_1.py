#!/usr/bin/env python

#Author: Elliot Willis
#Date: 2024-11-27

#Assumptions:
# 1. The mappings are stored in a directory called 'mappings' in the same directory as this script
# 2. The mappings are stored as json files that contain a single object taken from the 'd11r_mapping' key in the managedObject
# 3. Mappings maintain the same "ident" value throughout their lifecycle
# 4. Mapping version is analogous to "lastUpdate" field in the mapping i.e. a new version of a mapping will have a later "lastUpdate" timestamp

import requests, json, os
from requests.auth import HTTPBasicAuth

base_url = os.getenv('CUMULOCITY_URL') 
managedObject_url = "/inventory/managedObjects"

mappings_dir = 'mappings'

# find all mappings that are available in github
for filename in os.listdir(mappings_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(mappings_dir, filename)
        with open(filepath, 'r') as file:
            new_mapping = json.load(file)
        
            query_string = "query=$filter=(type+eq+'d11r_mapping'+and+d11r_mapping.ident+eq+'" + new_mapping['ident'] + "')"

            url = base_url + managedObject_url + "?" + query_string
            headers = {'Accept': 'application/json'}
            auth = HTTPBasicAuth(os.getenv('CUMULOCITY_USERNAME'), os.getenv('CUMULOCITY_PASSWORD'))
            
            resp = requests.request("GET", url, headers=headers, data='', auth=auth)
            current_mapping = json.loads(resp.text)['managedObjects'][0]['d11r_mapping'] #extract the mapping template from the managedObject

            if current_mapping['lastUpdate'] >= new_mapping['lastUpdate']:
                print(f'Mapping is up to date: "{current_mapping['name']}"')
                
            else:
                print(f'{current_mapping['name']} is not up to date')

                url = base_url + '/service/dynamic-mapping-service/mapping'
                headers = {'Content-Type': 'application/json'}
                auth = HTTPBasicAuth(os.getenv('CUMULOCITY_USERNAME'), os.getenv('CUMULOCITY_PASSWORD'))
                
                resp = requests.request("PUT", url, headers=headers, data=json.dumps(new_mapping), auth=auth)
                print(resp.text)

exit(0)