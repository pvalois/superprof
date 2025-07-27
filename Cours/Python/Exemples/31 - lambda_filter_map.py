#!/usr/bin/env python3

# Exemples d'utilisation de lambda, filter et map

# Liste d'exemples
nombres = list(range(1, 11))  # de 1 à 10

# 1. Utilisation de lambda pour créer une fonction anonyme
carre = lambda x: x ** 2

# 2. Utilisation de map pour appliquer carre à chaque élément
carres = list(map(carre, nombres))
print("Carrés des nombres de 1 à 10 :", carres)

# 3. Utilisation de filter pour filtrer les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print("Nombres pairs de 1 à 10 :", pairs)

# 4. Combiner map et filter : carrés des nombres pairs
carres_pairs = list(map(carre, filter(lambda x: x % 2 == 0, nombres)))
print("Carrés des nombres pairs :", carres_pairs)

# 5. Exemple avec **args et **kwargs dans une fonction lambda (un peu artificiel)
def appliquer_fonction(fonction, *args, **kwargs):
    return fonction(*args, **kwargs)

resultat = appliquer_fonction(lambda x, y=0: x + y, 5, y=3)
print("Résultat de la fonction lambda avec args et kwargs :", resultat)

