#!/bin/bash

a="$1"
b="$2"
c=$(date +%Y%m%d_%H%M%S)
d="b_$c.tar.gz"

if [ ! -d "$a" ]; then
    echo "Erreur"
    exit 1
fi

if [ ! -d "$b" ]; then
    mkdir -p "$b"
fi

tar -czf "$b/$d" "$a"

if [ $? -eq 0 ]; then
    echo "Succès"
else
    echo "Échec"
    exit 1
fi
