#!/bin/bash

fichier=${1}

if [[ -f "$fichier" ]]; then
    echo "Le fichier $fichier existe."
else
    echo "Le $fichier n'existe pas (ou n'est pas fichier)."
fi

