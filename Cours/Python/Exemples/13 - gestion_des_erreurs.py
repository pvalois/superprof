#!/usr/bin/env python3

# Exemple de gestion d’erreurs en Python

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : division par zéro impossible.")
        return None
    except TypeError:
        print("Erreur : les deux paramètres doivent être des nombres.")
        return None
    else:
        print(f"Résultat : {result}")
        return result
    finally:
        print("Fin de la fonction division.")

if __name__ == "__main__":
    division(10, 2)    # Résultat attendu
    division(10, 0)    # Division par zéro
    division(10, "a")  # Mauvais type

    # Lever une exception manuellement
    try:
        raise ValueError("Erreur personnalisée")
    except ValueError as e:
        print(f"Exception levée : {e}")

