#!/bin/bash
set -eu

pip3 --version
echo "Installing application dependencies"
pip3  install -r requirement.txt

#Debugging
echo "Printing pip freeze output .."
pip3 freeze