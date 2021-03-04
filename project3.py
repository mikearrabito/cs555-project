# CS 555 Group 5 Project 3
import os
import sys
import Family
import Person

gedcom_file_path = os.path.join(os.getcwd(), 'family.ged')

f = open(gedcom_file_path)

for line in f.readlines():
    line = line.rstrip()
    # FAM - id
    # INDI - person

