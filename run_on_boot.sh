#!/bin/bash
#File: trotter_codes/midterm/run_on_boot.sh

# Absolute path to Virtual Environment python interpreter
PYTHON=/home/pi/Desktop/trotter_codes/midterm/venv/bin/python

# Absolute path to Python script
SCRIPT=//home/pi/Desktop/trotter_codes/midterm/trotter_midterm.py

# Absolute path to output log file
LOG=/home/pi/Desktop/trotter_codes/midterm/midterm.log

echo -e "\n####### STARTUP $(date) ######\n" >> $LOG

$PYTHON $SCRIPT >> $LOG 2>&1
