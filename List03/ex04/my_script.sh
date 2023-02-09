#!/bin/sh

input="requirement.txt"

python3 -m venv django_venv
while IFS=input read -r line 
do
    echo $line
    .  $PWD/django_venv/bin/activate && pip install "$line" 
done < "$input" 
source  $PWD/django_venv/bin/activate
