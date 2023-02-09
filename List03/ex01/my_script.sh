#!/bin/sh

pip --version
pip install --target=local_lib --force-reinstall git+https://github.com/jaraco/path.git > install.log
python3 ./my_program.py