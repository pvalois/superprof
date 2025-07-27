#!/usr/bin/env python3 

# Recherche simple d’une chaîne dans un fichier, façon grep

def grep_like(fichier, motif):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for num, ligne in enumerate(f, 1):
                if motif in ligne:
                    print(f"{num}: {ligne.strip()}")
    except FileNotFoundError:
        print(f"Erreur : fichier '{fichier}' non trouvé.")

if __name__ == "__main__":
    fichier = "exemple.txt"  # Remplacer par ton fichier
    motif = "erreur"         # Motif à chercher
    grep_like(fichier, motif)
