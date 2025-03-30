#!/bin/bash

echo "Entrez le répertoire : "
read source_dir

if [ ! -d "$source_dir" ]; then
    echo "Erreur !"
    exit 1
fi

echo "Entrez le répertoire : "
read dest_dir

if [ ! -d "$dest_dir" ]; then
    echo "Erreur !"
    mkdir -p "$dest_dir"
fi

backup_file="$dest_dir/backup_$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$backup_file" "$source_dir"

if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "KO"
    exit 1
fi

output_file="$dest_dir/backup_log.txt"
echo "$(date +%Y-%m-%d\ %H:%M:%S) : Sauvegarde de $source_dir vers $backup_file" >> "$output_file"


