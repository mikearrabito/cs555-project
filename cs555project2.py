# Michael Arrabito CS555 Project 2
import os
import sys
import Family
import Person

gedcom_file_path = os.path.join(os.getcwd(), 'family.ged')

f = open(gedcom_file_path)


def is_tag_valid(tag):
    set_of_valid_tags = {'INDI', 'NAME', "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL",
                         "DIV", "DATE", "HEAD", "TRLR", "NOTE"}
    return tag in set_of_valid_tags


for line in f.readlines():
    line = line.rstrip()
    print("--> " + line)
    split = line.split(" ", 2)
    level = split[0]
    tag = split[1]
    rest = ""
    if len(split) > 2:
        rest = split[2]
        if rest == 'FAM' or rest == 'INDI':
            tag = rest  # exception to tag being second value in line
            rest = split[1]  # print the id at the end of our output string
    valid = is_tag_valid(tag)
    if valid:
        valid = 'Y'
    else:
        valid = 'N'

    print("<-- " + level + "|" + tag + "|" + valid + "|" + rest)

