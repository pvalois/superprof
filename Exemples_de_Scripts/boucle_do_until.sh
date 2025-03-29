#!/bin/bash

count=1

until [ $count -gt 5 ]
do
    echo "Le compteur est $count"
    ((count++))  # incrémentation de count
done
