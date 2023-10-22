import requests

BASE = "http://127.0.0.1:5000/"

# Get Test
get_response = requests.get(BASE + "dalimember/Amon Ferri")
print(get_response.json())

# Put Test
put_response = requests.put(BASE + "dalimember/Andy",
                            {
                                "year": "2023",
                                "dev": True,
                                "des": False,
                                "pm": False,
                                "core": False,
                                "mentor": False,
                                "major": "Computer Science",
                                "minor": "Digital Art",
                                "birthday": "05-06",
                                "home": "New York, New York",
                                "quote": "...",
                                "favorite thing 1": "Fresh pineapple",
                                "favorite thing 2": "Wintermint",
                                "favorite thing 3": "Sunny days",
                                "favorite dartmouth tradition": "Lobster bisque",
                                "fun fact": "Whales are real",
                                "picture": "https://api.typeform.com/responses/files/39f37747544d2be7038e60d7637f1f4e6d587f239c4bfbc1ecf3457ff05391d6/owlbear.png"
                            })
print(put_response.json())