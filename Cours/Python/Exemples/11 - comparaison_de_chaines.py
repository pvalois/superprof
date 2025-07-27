#!/usr/bin/env python3

# Trouver les mots communs entre deux textes

import string

texte1 = """
Python est un langage de programmation très populaire.
Il est utilisé dans de nombreux domaines, tels que la science des données,
le développement web, et bien d'autres.
"""

texte2 = """
Le langage Python est apprécié pour sa simplicité.
De nombreux développeurs utilisent Python pour le web et la science.
"""

def nettoyer_texte(texte):
    # Mettre en minuscules
    texte = texte.lower()
    # Retirer la ponctuation
    return texte.translate(str.maketrans('', '', string.punctuation))

def mots_communs(t1, t2):
    mots1 = set(nettoyer_texte(t1).split())
    mots2 = set(nettoyer_texte(t2).split())
    return mots1.intersection(mots2)

def mots_uniques(t1, t2):
    mots1 = set(nettoyer_texte(t1).split())
    mots2 = set(nettoyer_texte(t2).split())
    uniques_t1 = mots1.difference(mots2)
    uniques_t2 = mots2.difference(mots1)
    return uniques_t1, uniques_t2

if __name__ == "__main__":
    communs = mots_communs(texte1, texte2)

    print("Mots communs aux deux textes :")
    print (sorted(communs))

    uniques1, uniques2 = mots_uniques(texte1, texte2)

    print("Mots uniques au premier texte :")
    print(sorted(uniques1))
    print("Mots uniques au second texte :")
    print(sorted(uniques2))

