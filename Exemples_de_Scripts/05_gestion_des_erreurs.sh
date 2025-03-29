
#!/bin/sh

## Exécuter une commande puis une autre si la première réussit
mkdir dossier && rmdir dossier 

## Exécuter une commande puis une autre en cas d'échec de la première
mkdir /dossier || echo Impossible de créer le dossier

## Récuperer le code d'erreur de la dernière commande lancée 
mkdir /dossier
echo $?  # ici le code d'erreur 1 signal un échec de la commande

# Arrêter le script en cas d'erreur
set -e

