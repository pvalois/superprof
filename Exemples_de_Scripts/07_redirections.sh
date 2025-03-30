#!/bin/sh

echo "Hello" > fichier.txt  # Écrit dans fichier.txt (écrase l'ancien contenu)
echo "Ajout" >> fichier.txt  # Ajoute à la fin du fichier

ls | grep ".sh"  # Filtrer la sortie d'une commande

ls non_existant 2> erreur.log  # Capture les erreurs (2 est le flux stderr)

