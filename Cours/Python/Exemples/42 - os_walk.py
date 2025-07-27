#!/usr/bin/env python3

# Exemple d'utilisation de os.walk pour parcourir un répertoire

import os

def parcourir_dossier(racine):
    """
    Parcourt récursivement le dossier 'racine' et affiche dossiers et fichiers.
    """
    for dossier_courant, sous_dossiers, fichiers in os.walk(racine):
        print(f"Dossier : {dossier_courant}")
        print(f"  Sous-dossiers : {sous_dossiers}")
        print(f"  Fichiers : {fichiers}")

if __name__ == "__main__":
    chemin = "."  # dossier courant
    print(f"Parcours du dossier {chemin} :\n")
    parcourir_dossier(chemin)

