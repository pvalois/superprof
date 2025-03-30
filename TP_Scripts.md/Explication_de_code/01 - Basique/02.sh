#!/bin/bash

fichier="mon_fichier.txt"

while IFS= read -r ligne; do
    echo "Ligne lue : $ligne"
done < "$fichier"

