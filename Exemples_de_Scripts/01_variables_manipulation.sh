#!/bin/bash

### Extration de parties de la chaine 

mydate=$(date +"%Y%m%d")    #Affecte le resultat d'une commande a une varible

Year=${mydate:0:4}
Month=${mydate:4:2}
Day=${mydate:6:2}

echo "$Day/$Month/$Year"

### Récuperation de partie gauche 

mydate="12-2-1994"
Year=${mydate: -4}

echo "$Year"

### Split par pattern

filename="exemple.txt"

echo ${filename%.txt}.c    #Supprime la terminaison .txt et ajoute .c
echo ${filename#*ple}      #Supprime le prefixe *ple, ne laissant que .txt

## Autres transformations 

texte="Super Bash Script"

echo "Longueur : ${#texte}"
echo "Majuscules : ${texte^^}"
echo "Minuscules : ${texte,,}"
