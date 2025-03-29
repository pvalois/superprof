#!/bin/bash

panier=("choux" "patates" "carottes")
for legume in "${panier[@]}"; do
  echo $legume
done
