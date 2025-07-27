#!/usr/bin/env python3 

# Exemples d’utilisation du module datetime

from datetime import datetime, timedelta

def afficher_date_heure_actuelle():
    maintenant = datetime.now()
    print("Date et heure actuelles :", maintenant)

def afficher_date_formatee(date_obj):
    print("Date formatée :", date_obj.strftime("%d/%m/%Y %H:%M:%S"))

def ajouter_jours(date_obj, jours):
    return date_obj + timedelta(days=jours)

def calcul_difference(date1, date2):
    diff = date2 - date1
    print(f"Différence entre les dates : {diff.days} jours")

if __name__ == "__main__":
    afficher_date_heure_actuelle()

    date1 = datetime(2025, 7, 27, 12, 0, 0)
    afficher_date_formatee(date1)

    date2 = ajouter_jours(date1, 10)
    afficher_date_formatee(date2)

    calcul_difference(date1, date2)

