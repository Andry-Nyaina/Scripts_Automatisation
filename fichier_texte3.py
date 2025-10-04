import os.path

filename = "nom_fichier.txt"

if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas")


"""try:
    f = open(filename, "r")
except:
    print("ERREUR: Le fichier n'a pas pu ouvrir, car il n'xiste pas")
else:
    texte = f.read()
    print(texte)
    f.close"""