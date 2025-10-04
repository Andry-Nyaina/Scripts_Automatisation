
f = open("nom_fichier.txt", "r")

"""texte = f.read()
print(texte)"""

"""texte = f.readline()
print(texte, end="")
texte = f.readline()
print(texte)"""

# texte = f.readlines()
# print(texte)

for line in f:
    print(line, end="")

f.close()