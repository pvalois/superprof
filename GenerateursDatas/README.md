Ces deux script génèrent 10 fichiers de 1000 lignes de données, respectivement :

- **generate_name.py** : nom, prenom, genre
- **generate_fake_adn.py** : sequence adn, couleurs d'yeux, couleurs de cheveux, genre, cancer 

Le but de ces données est de travailler les commandes unix suivantes :

- cat : afficher le contenu d'un ou plusieurs fichier 
- grep : chercher une ligne ou un motif dans un fichier
- cut : découper les données pour les retraiter
- sort : trier les données 
- uniq : supprimer les doublons
- tr : effectuer des transformations

Chaque commence dispose d'une aide disponible avec les commandes : 

```bash
man <commande>
info <commande>
```

et de façon plus avancée : 

- sed : modifications des données 
- awk : traitement des données
- for, if : pour les boucles et conditions

ansi que les méchanismes de pipe \| et de redirection \< et \>

Le type de recherche qui peuvent être faites : 

- extractions de tous les prénom pour un meme nom de famille
- compter les filles et les garcons 
- faire des statistiques de repartition de couleurs des yeux et cheveux
- voir si il existe une correlation entre couleurs des yeux, cheveux et cancer 

Voila un petit ensemble d'idées permettant de réflechir à : 

- comprendre la structure des données et leurs propriétés 
- scripter l'extraction des données et/ou leur propriétés
- effectuer des modification ou décompte des résultats

Tout cela dans le but général de : 

- Comprendre les commandes basiques d'un script shell 
- Comprendre le travail d'extraction de données
- Comprendre la possibilité de procéder à des recherches/calculs sur ces données
