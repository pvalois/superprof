#!/bin/bash

echo "Entrez une extension (ex: txt, jpg):"
read ext

find . -type f -name "*.$ext"

