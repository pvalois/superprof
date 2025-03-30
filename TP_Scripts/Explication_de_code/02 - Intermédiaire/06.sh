#!/bin/bash

kk="$1"

ll=$(curl -Is "$kk" | head -n 1)

if echo "$ll" | grep -q "200"; then
    echo "ca marche"
else
    echo "ca marche pas"
    exit 1
fi
