# Surveiller l’espace disque

Ecrire un script qui envoie une alerte si l’espace libre descend sous un certain seuil :

* Le seuil est donné en argument sous forme de pourcentage
* Toute partition dépassant ce seuil sont notifiées, sauf si une partition précise est spécifiée en deuxième argument

# Vérifier si un processus tourne

Vérifier si un service tourne :

* Le service doit être donné en argument
* Le service doit être redémarré si inactif

# Automatiser la sauvegarde

Ecrire un script qui archive un dossier et l’envoie sur un serveur distant via scp ou rsync

* Les informations du serveur doivent être précisés sous forme de variable
* Un fichier de log daté doit être généré

# Dirty monitoring 

* Ecrire un script qui éxecutera une commande informative (ex: df -h)
* A chaque nouvelle exécution du script elle ne doit nous afficher que les différences avec la précédente exécution
* Info : il faudra utiliser une trace pour savoir comment c'était avant, et bien sur, maintenir cette trace :)
