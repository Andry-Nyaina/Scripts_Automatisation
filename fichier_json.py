import json

"""personne = {
    "nom" : "Draken",
    "age" : 22,
    "ami" : ["Mickey", "Takimichi", "Baji"]
}


personne_json = json.dumps(personne)

print(f"Presonne : {personne_json}")

f = open("fichier_json.txt", "w")
f.write(personne_json)
f.close"""

f = open("fichier_json.txt", "r")
donnes_json = f.read()
f.close()

#recuperer un dictionnaire a nouveau
personne = json.loads(donnes_json)
print(type(personne))
print(f"Nom: {personne["nom"]}")
