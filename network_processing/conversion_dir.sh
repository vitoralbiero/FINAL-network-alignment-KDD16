#!/bin/bash

mkdir $2

for filename in "$1"*.gw; do
    echo "$filename"
    OUTY=$(echo "$filename" | cut -d'.' -f 1 | rev | cut -d'/' -f 1 | rev )
    echo "$2$OUTY"
    python3 FINAL-network-alignment-KDD16/network_processing/conversion.py "$filename" -o "$2$OUTY.csv"
done
