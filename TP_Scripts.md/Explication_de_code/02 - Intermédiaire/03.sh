#!/bin/bash

temp_dir="/tmp"
log_dir="/var/log"

find "$temp_dir" -type f -mtime +7 -exec rm -f {} \;
find "$log_dir" -type f -name "*.log" -mtime +30 -exec rm -f {} \;

if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "KO"
    exit 1
fi
