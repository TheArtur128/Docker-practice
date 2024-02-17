#!/bin/ash

name=$NAME

if [ $name = "" ]
then
	name="unknown"
fi

echo "Hello $name!"

