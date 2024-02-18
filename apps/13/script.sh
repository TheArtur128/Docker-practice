#!/bin/bash

smiles=(":D" ":P" ":X" "D/")

while [ 0 ]; do
    for smile in ${smiles[*]}; do
	    echo "$smile"
	    sleep 0.2
    done
done

