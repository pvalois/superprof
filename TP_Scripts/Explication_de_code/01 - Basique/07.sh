#!/bin/bash

echo "Entrez le nom de fichier : "
read file
chmod 755 "$file" || exit 1
