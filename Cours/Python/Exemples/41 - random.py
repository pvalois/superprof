#!/usr/bin/env python3 

# Exemples d’utilisation du module random avec seed

import random
import datetime

def initialiser_seed(seed=None):
    """Initialise la graine du générateur aléatoire"""
    random.seed(seed)
    print(f"Seed initialisée à : {seed}")

def tirage_aleatoire_entier(minimum, maximum):
    """Retourne un entier aléatoire entre minimum et maximum inclus"""
    return random.randint(minimum, maximum)

def tirage_aleatoire_flottant():
    """Retourne un flottant aléatoire entre 0 et 1"""
    return random.random()

def melanger_liste(liste):
    """Mélange les éléments d’une liste en place"""
    copy=list(liste)
    random.shuffle(copy)
    return(copy)

def choix_aleatoire(liste):
    """Choisit un élément aléatoire dans une liste"""
    return random.choice(liste)

if __name__ == "__main__":
    initialiser_seed(42)  # On fixe la seed pour la reproductibilité

    print("Entier aléatoire entre 1 et 10 :", tirage_aleatoire_entier(1, 10))
    print("Flottant aléatoire entre 0 et 1 :", tirage_aleatoire_flottant())

    initialiser_seed() # On fixe la seed sur l'heure systeme

    fruits = ["pomme", "banane", "cerise", "datte"]
    print("Liste :", fruits, "->", melanger_liste(fruits))

    fruit_choisi = choix_aleatoire(fruits)
    print("Fruit choisi au hasard :", fruit_choisi)

