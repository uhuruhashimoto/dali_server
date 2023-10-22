# Loads JSON data into db at startup

import json
import requests

BASE = "http://127.0.0.1:5000/"
filename = "dali_social_media.json"
name_keyword = "name"
members = {}

# Load file data and store by sequential ID
f = open(filename)
members = json.load(f)
id=0
for member in members:
    get_response = requests.put(BASE + f"dalimember/{id}")
    print(get_response.json())
    id+=1
f.close()

