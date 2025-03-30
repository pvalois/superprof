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
