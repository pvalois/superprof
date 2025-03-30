#!/bin/bash

# Fonction 1
f1() {
    local a="$1"
    local b="$2"
    local c="$3"
    echo "Argument 1: $a"
    echo "Argument 2: $b"
    echo "Argument 3: $c"
}

# Fonction 2
f2() {
    local x="$1"
    local y="$2"
    local z="$3"
    echo "Traitement sur $x, $y et $z"
}

# Fonction 3
f3() {
    local p="$1"
    local q="$2"
    echo "Processus avec $p et $q"
}

# Fonction 4
f4() {
    local m="$1"
    local n="$2"
    echo "Opération sur $m et $n"
}

# Fonction principale
main() {
    if [ "$#" -lt 3 ]; then
        echo "Erreur d'usage"
        exit 1
    fi

    f1 "$1" "$2" "$3"
    f2 "$4" "$5" "$6"
    f3 "$7" "$8"
    f4 "$9" "${10}"
}

# Lancer le script
main "$@"
