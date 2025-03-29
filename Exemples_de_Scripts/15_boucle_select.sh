#!/bin/bash

echo "Choisissez une option :"
select choix in "Option 1" "Option 2" "Quitter"
do
    case $choix in
        "Option 1") echo "Vous avez choisi Option 1" ;;
        "Option 2") echo "Vous avez choisi Option 2" ;;
        "Quitter") exit 0 ;;
        *) echo "Choix invalide" ;;
    esac
done
