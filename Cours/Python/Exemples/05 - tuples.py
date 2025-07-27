#!/usr/bin/env python3  

# Introduction aux listes et tuples

# Liste : modifiable
notes = [12, 15, 14, 9, 17]
print("Notes :", notes)

# Accès et modification
print("Première note :", notes[0])
notes[2] = 16
print("Notes après modification :", notes)

# Ajouter et supprimer
notes.append(18)
print("Notes après append :", notes)
notes.remove(9)
print("Notes après remove(9) :", notes)

# Quelques fonctions utiles
print("Nombre de notes :", len(notes))
print("Note maximale :", max(notes))
print("Note moyenne :", sum(notes) / len(notes))

# Trier sans modifier l’original
print("Notes triées (sans modifier la liste) :", sorted(notes))

# Trier en place
notes.sort()
print("Notes triées (modification en place) :", notes)

# Boucle sur la liste
print("Affichage des notes avec leur index :")
for i, note in enumerate(notes):
    print(f"Note {i} : {note}")

# Tuple : non modifiable
coord = (48.85, 2.35)  # Latitude, Longitude

print("Coordonnées de Paris :", coord)
print("Latitude :", coord[0])
print("Longitude :", coord[1])

# Erreur si on tente de modifier un tuple
try:
    coord[0] = 50.0
except TypeError as e:
    print("Erreur attendue :", e)

