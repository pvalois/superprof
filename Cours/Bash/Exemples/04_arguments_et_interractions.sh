#!/bin/bash

echo "Nombre d'arguments passés : $#"
echo "Premier argument : $1"

# Moditification du séparateur IFS (Internal Field Separator)

f="bonjour monsieur durand"
for i in $f ; do echo $i ; done

f="mon:separateur:est:deux:points"
IFS=":"
for i in $f ; do echo $i ; done

# Réinitialiser IFS à son état par défaut

IFS=$' \t\n'

# Demande de réponse clavier

echo "Votre nom ?"
read nom
echo "Bonjour, $nom !"

