#!/usr/bin/env python3  

# Exemples simples de manipulations de chaînes

texte = "Bonjour, les étudiants de Superprof !"

# Longueur de la chaîne
print("Longueur :", len(texte))

# Accès à un caractère
print("Premier caractère :", texte[0])
print("Dernier caractère :", texte[-1])

# Slicing (sous-chaînes)
print("Les 7 premiers caractères :", texte[:7])
print("Les mots à partir du 3e mot :", texte.split()[2:])

# Mise en majuscules / minuscules
print("Majuscules :", texte.upper())
print("Minuscules :", texte.lower())

# Remplacement de mots
print("Remplacement de 'Superprof' par 'Python' :", texte.replace("Superprof", "Python"))

# Comptage d'un mot
print("Nombre de fois 'de' :", texte.count("de"))

# Découpage en mots
mots = texte.split()
print("Liste des mots :", mots)

# Reconstruction avec join
texte_reconstruit = " | ".join(mots)
print("Texte reconstruit avec | :", texte_reconstruit)
