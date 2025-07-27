#!/usr/bin/env python3 

# Introduction aux dictionnaires

# Un dictionnaire classique : noms et âges
ages = {
    "Alice": 23,
    "Bob": 31,
    "Charlie": 19
}

# Accès
print("Âge de Bob :", ages["Bob"])

# Ajout et modification
ages["Diana"] = 28
ages["Alice"] = 24
print("Dictionnaire après modifications :", ages)

# Suppression
del ages["Charlie"]
print("Après suppression de Charlie :", ages)

# Boucle sur les clés et valeurs
print("Parcours des âges :")
for nom, age in ages.items():
    print(f"{nom} a {age} ans")

# Vérification d'existence
if "Eve" not in ages:
    print("Eve n’est pas dans le dictionnaire.")

