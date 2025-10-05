import requests
import json


# API REST
"""reponse = requests.get("https://codeavecjonathan.com/res/pizzas1.json")

if reponse.status_code == 200:
    reponse.encoding = "utf-8"
    print(reponse.text)
    pizzas = json.loads(reponse.text)
    print(f"Nombres des pizzas : {len(pizzas)}")
else:
    print(f"ERREUR code : {reponse.status_code}")"""

reponse = requests.get("https://codeavecjonathan.com/res/exemple.html")

if reponse.status_code == 200:
    reponse.encoding = "utf-8"
    print(reponse.text)
else:
    print(f"ERREUR code : {reponse.status_code}")