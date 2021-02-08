#!/bin/bash
set -eu

#####
echo "Running application"
#####
cd /usr/sbin && python3 run.py -D FOREGROUND