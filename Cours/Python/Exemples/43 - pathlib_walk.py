#!/usr/bin/env python3

# Parcours récursif d'un dossier avec pathlib

from pathlib import Path

def parcourir_dossier(racine):
    """
    Parcourt récursivement le dossier 'racine' et affiche dossiers et fichiers.
    """
    racine = Path(racine)
    for chemin in sorted(racine.rglob('*')):
        if chemin.is_dir():
            print(f"Dossier : {chemin}")
        elif chemin.is_file():
            print(f"Fichier : {chemin}")

if __name__ == "__main__":
    chemin = "."  # dossier courant
    print(f"Parcours du dossier {chemin} avec pathlib :\n")
    parcourir_dossier(chemin)

