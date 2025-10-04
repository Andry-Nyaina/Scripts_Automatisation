# Script simple pour écrire du texte dans un fichier avec Python

# Ouvre (ou crée) le fichier en mode ajout
f = open("nom_fichier.txt", "w")

# Exemple 1 : écrire une seule phrase
# f.write("Bonjour\n")

# Exemple 2 : écrire plusieurs phrases avec writelines()
# l = ["première phrase\n", "deuxième phrase\n", "troisième phrase\n"]
# f.writelines(l)

# Exemple 3 : écrire plusieurs phrases avec join()
l = ["première phrase", "deuxième phrase", "troisième phrase"]
f.write("\n".join(l))
f.write("\nFin")

f.close()
print("Écriture terminée")
