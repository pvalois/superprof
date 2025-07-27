#!/usr/bin/env python3 

# Exemples de fonctions avec ou sans annotations de type

# Fonction sans annotation
def saluer(nom):
    print(f"Bonjour, {nom} !")

# Fonction avec annotation simple (juste variable : type, sans import)
def addition(a: int, b: int = 0) -> int:
    return a + b

# Fonction sans annotation avec *args et **kwargs
def somme_args(*args):
    return sum(args)

def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} = {valeur}")

# Fonction avec annotation et retour typé
def factorielle(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)

# Exemple avec annotation simple
def maximum(*valeurs: int) -> int:
    if not valeurs:
        return None
    return max(valeurs)

if __name__ == "__main__":

    saluer("Alice")
    print("Addition 3 + 4 =", addition(3, 4))
    print("Addition 5 =", addition(5))

    print("Factorielle de 5 =", factorielle(5))
    print("Somme des arguments 1, 2, 3, 4 :", somme_args(1, 2, 3, 4))

    afficher_infos(nom="Alice", age=30, ville="Paris")

    print("Maximum de 3, 7, 2 :", maximum(3, 7, 2))

