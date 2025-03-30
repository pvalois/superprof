#!/bin/bash

echo -n "Fichier : "
read file

echo -n "Repertoire : "
read dir

cp "$file" "$dir" || echo "Opération impossible"
