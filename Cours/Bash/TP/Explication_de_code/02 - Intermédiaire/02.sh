#!/bin/bash

CPU_THRESHOLD=80
DESTI="admin@example.com"
high_cpu_processes=$(ps aux --sort=-%cpu | awk -v threshold=$CPU_THRESHOLD '$3 > threshold {print $1, $3, $11}' | head -n 5)

if [ ! -z "$high_cpu_processes" ]; then
    echo "processus > $CPU_THRESHOLD%  : $high_cpu_processes"
    echo "Information doit être reportée a $DESTI"
else
    echo "tout va bien"
fi

# Vérification de la mémoire utilisée
MEMORY_THRESHOLD=90
high_memory_processes=$(ps aux --sort=-%mem | awk -v threshold=$MEMORY_THRESHOLD '$4 > threshold {print $1, $4, $11}' | head -n 5)

# Si des processus consomment trop de mémoire, envoyer une autre alerte
if [ ! -z "$high_memory_processes" ]; then
    echo "processus > $MEMORY_THRESHOLD%  : $high_memory_processes" 
    echo "Information doit être reportée a $DESTI"
else
    echo "tout va bien"
fi

