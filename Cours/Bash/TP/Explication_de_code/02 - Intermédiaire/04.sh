#!/bin/bash

echo "Choisissez une option:"
echo "1 : blah blah"
echo "2 : bli bli"
echo "3 : gazomebu"
read option

case $option in
    1)
        echo "Entrez le nom d'utilisateur :"
        read username
        sudo useradd "$username"
        sudo passwd "$username"
        ;;
    2)
        echo "Entrez le nom de l'utilisateur :" 
        read username
        sudo userdel -r "$username"
        ;;
    3)
        echo "Entrez le nom d'utilisateur :"
        read username
        sudo passwd "$username"
        ;;
    *)
        echo "Whut whut whut ?"
        ;;
esac
