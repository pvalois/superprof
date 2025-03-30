#!/bin/bash

mm=("$@")

for dir in "${mm[@]}"; do
    mkdir -p "$dir"
done
