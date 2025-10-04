# SDLITE : LECTURE DE LA TABLE

import sqlite3

connexion = sqlite3.connect("album.db")
curseur = connexion.cursor()

curseur.execute("SELECT * FROM artistes")
artistes = curseur.fetchall()
print(artistes)

connexion.close()