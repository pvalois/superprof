#!/bin/bash

sleep 10 &  # Lance un processus en arrière-plan
echo "Processus lancé avec PID $!"

jobs # liste les jobs actifs

ps -ef # liste tous les processus avec leurs informations principales
ps -efT # liste tous les process et leurs threads
ps -fU $LOGNAME # N'affiche que les process du compte loggué

pstree # Affiche l'arbre de parenté des processus en cours 
pgrep -al firefox # Recherche un processus par son nom
