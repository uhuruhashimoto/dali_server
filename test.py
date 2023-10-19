import requests

BASE = "http://127.0.0.1:5000/"

# Get Test
get_response = requests.get(BASE + "dalimember/bob")
print(get_response.json())

# Post Test
put_response = requests.put(BASE + "dalimember/andy", {"major": "math"})
print(put_response.json())