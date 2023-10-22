# Loads JSON data into db at startup

import json
import requests

BASE = "http://127.0.0.1:5000/"
filename = "dali_social_media.json"

# Load file data and store by sequential ID
print(f"Opening file {filename}...")
f = open(filename)
print(f"Loading JSON from {filename}...")
members = json.load(f)
for id, member in enumerate(members):
    get_response = requests.put(BASE + f"dalimember/{id}", member)
    print(get_response.json())
print(f"Closing {filename}...")
f.close()
print("Done.")

