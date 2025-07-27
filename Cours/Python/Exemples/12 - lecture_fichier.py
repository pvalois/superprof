#!/usr/bin/env python3 

# Lire un fichier texte ligne par ligne

if __name__ == "__main__":

    nom_fichier = "exemple.txt"  # Remplace par le chemin vers ton fichier

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            for i, ligne in enumerate(f, 1):
                print(f"Ligne {i}: {ligne.strip()}")
    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")


