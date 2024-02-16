#!/bin/ash

filename="smile.txt"

if [ -f "$filename" ]; then
	echo "File \"$filename\" is not ignored :O"
else
	echo "File \"$filename\" is ignored D/"
fi

