#!/bin/bash

fichier=${1}

if [[ -f "$fichier" ]]; then
    echo "Le fichier $fichier existe."
else
    echo "Le fichier $fichier n'existe pas."
fi

