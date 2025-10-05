import requests 

reponse = requests.get("https://images3.alphacoders.com/134/1342304.jpeg")

if reponse.status_code == 200:
    f = open("One-Piece.jpeg", "wb")
    f.write(reponse.content)
    f.close()
    print("Ecriture terminée")
else:
    print(f"ERREUR : {reponse.status_code}")