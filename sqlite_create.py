# SQLITE : CREATION TABLE

import sqlite3

# connexion = "album.db"
# executer / commit
# commit 
# fermer 

connexion = sqlite3.connect("album.db")
curseur = connexion.cursor()


curseur.execute("""CREATE TABLE artistes (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE albums (
                almbum_id INTEGER NOT NULL PRIMARY KEY,
                artiste_id INTEGER REFERENCES artistes,
                titre VARCHAR,
                anne_sortie INTEGER);""")

curseur.execute("""INSERT INTO artistes (nom) VALUES ("Michael Jackson");""")
mj_id = curseur.lastrowid
curseur.execute("""INSERT INTO artistes (nom) VALUES ("Celine Dion");""")
cd_id = curseur.lastrowid

curseur.execute(f"""INSERT INTO albums (artiste_id, titre, anne_sortie) VALUES ({mj_id}, "Thriller", 1982);""")
curseur.execute(f"""INSERT INTO albums (artiste_id, titre, anne_sortie) VALUES ({cd_id}, "Let's Talk About Love", 1997);""")
curseur.execute(f"""INSERT INTO albums (artiste_id, titre, anne_sortie) VALUES ({cd_id}, "Falling into You", 1996);""")
curseur.execute(f"""INSERT INTO albums (artiste_id, titre, anne_sortie) VALUES ({mj_id}, "Bad", 1987);""")

connexion.commit()
connexion.close()
