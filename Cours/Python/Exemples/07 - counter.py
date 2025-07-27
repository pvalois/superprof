#!/usr/bin/env python3 

# Initiation a counter

from collections import Counter

phrase = "le python est simple et le python est puissant"
mots = phrase.split()
compteur = Counter(mots)

print("\nOccurrences des mots :")
for mot, nb in compteur.items():
    print(f"{mot} : {nb}")

