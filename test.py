import requests

BASE = "http://127.0.0.1:5000/"

# Get Test
get_response = requests.get(BASE + "dalimember/bob")
print(get_response.json())

# Post Test
post_response = requests.post(BASE+ "dalimember/bob")
print(post_response.json())