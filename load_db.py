# Loads JSON data into db at startup

import json
import requests

BASE = "http://127.0.0.1:5000/"
filename = "dali_social_media.json"

# Load file data and store by sequential ID
print(f"Loading JSON from {filename} into database...")
f = open(filename)
members = json.load(f)
for i, member in enumerate(members):
    get_response = requests.post(BASE + f"dalimember/{i}", member)
    print(get_response.json())
f.close()
print("...Done.")

