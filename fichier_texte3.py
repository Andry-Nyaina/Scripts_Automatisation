filename = "nom_fichier.txt"

try:
    f = open(filename, "r")
except:
    print("ERREUR: Le fichier n'a pas pu ouvrir, car il n'xiste pas")
else:
    texte = f.read()
    print(texte)
    f.close