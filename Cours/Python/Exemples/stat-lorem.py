#!/usr/bin/env python3 

import lorem
import shlex
from collections import Counter

t = lorem.text()

def compter_mots(texte):
    # On nettoie le texte : on met en minuscules, et on retire la ponctuation
    texte = texte.lower()
    mots = shlex.shlex(texte)
    
    # Utilise Counter pour compter les occurrences
    return dict(Counter(mots))

# Exemple d'utilisation
if __name__ == "__main__":
    t = lorem.text()
    print("Texte généré : \n")
    print(t.strip())
    print("")

    print("Occurrences des mots : \n")
    stats=compter_mots(t.strip())

    for k in sorted(stats):
        if (k=="."): continue
        print(f"{k} : {stats[k]}")
