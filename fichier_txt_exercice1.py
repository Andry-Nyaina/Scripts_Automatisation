#Exercice: Ecrire 1 jusq'à 10 dans le fichier

f = open("fichier_texte_exercice1.txt", "w")

for i in range(1,11):
    f.write(f"{i}\n")

f.close()