#!/bin/bash

# Ce script s'utilise en precisant plus de 3 arguments pour bien comprendre

# la fonction shift permet de depiler des arguments et comme elle dépile, ces arguments deviennent perdus, mais ...

# Sauvegarder $@ dans un tableau
args=("$@")

# Afficher les arguments avant shift
echo "Avant shift: ${args[@]}"

# Shift des arguments
shift ; echo "Après shift: $@"
shift ; echo "Après deuxieme shift: $@"

# Restaurer les arguments originaux à partir du tableau
set -- "${args[@]}"

# Afficher les arguments restaurés
echo "Arguments restaurés: $@"
