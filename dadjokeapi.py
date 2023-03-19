import requests

url = "https://icanhazdadjoke.com/"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

joke = response.json()["joke"]

print("I've got a joke for you:\n" + joke)