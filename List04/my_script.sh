#!/bin/bash

/usr/bin/python3 -m venv django_venv
source ./django_venv/bin/activate
python -m pip install --force-reinstall -r requirement.txt