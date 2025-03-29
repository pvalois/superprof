#!/bin/sh

VAR=16

if [ "$VAR" -eq 10 ]; then
    echo "VAR vaut 10"
elif [ "$VAR" -gt 10 ]; then
    echo "VAR est supérieur à 10"
else
    echo "VAR est inférieur à 10"
fi
