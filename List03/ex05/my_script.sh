#!/bin/sh

input="requirement.txt"

python3 -m venv Django
while IFS=input read -r line 
do
    echo $line
    .  $PWD/Django/bin/activate && pip install "$line" 
done < "$input" 
source  $PWD/Django/bin/activate
