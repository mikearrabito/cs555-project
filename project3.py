# CS 555 Group 5 Project 3
import os
import sys
import Family
import Person
from prettytable import PrettyTable

gedcom_file_path = os.path.join(os.getcwd(), 'family.ged')

families = list()
people = list()

f = open(gedcom_file_path)
id = None
new_person = None
new_family = None
birt = False
deat = False

for line in f.readlines():
    line = line.rstrip()
    line = line.split(' ', 2)
    person = None
    if len(line) > 2 and line[2] == 'INDI':
        if new_person:
            # if we have started working on a person already, append that and create a new one to get info for
            people.append(new_person)
        id = line[1]
        new_person = Person.Person()
        # INDI comes first for each person, so if we reached a new id we can create a new person to add
        new_person.set_ID(id)

    if line[1] == 'NAME':
        name = line[2]
        name = name.replace('/', '')
        new_person.set_name(name)

    if line[1] == 'SEX':
        sex = line[2]
        new_person.set_gender(sex)

    if line[1] == 'BIRT':
        birt = True # if next date is a birthday

    if line[1] == 'DEAT':
        deat = True

    if line[1] == 'DATE' and birt:
        dob = line[2]
        new_person.set_birthday(dob)
        birt = False

    if line[1] == 'DATE' and deat:
        date_of_death = line[2]
        new_person.set_death(date_of_death)
        deat = False
        
    if line[1] == 'FAMS':
        new_person.set_spouse(line[2])

    if line[1] == 'FAMC':
        new_person.set_fam(line[2])  # child of this family

    if len(line) > 2 and line[2] == 'FAM':
        if new_person:
            # we are at start of families tags, all people are now added
            people.append(new_person)
            new_person = None
        if new_family:
            # if we created a family already, append it then start next
            families.append(new_family)
        new_family = Family.Family(line[1])  # create new family with id from line

    if len(line) > 2 and line[1] == 'HUSB':
        new_family.add_husband(line[2])

    if len(line) > 2 and line[1] == 'WIFE':
        new_family.add_wife(line[2])

    if len(line) > 2 and line[1] == 'CHIL':
        new_family.add_child(line[2])

    if len(line) > 2 and line[1] == '_CURRENT':
        if line[2] == 'N':
            new_family.divorced = True

for family in families:
    for person in people:
        if family.wife == person.id:
            family.add_wife(person)
        elif family.husband == person.id:
            family.add_husband(person)

pt1 = PrettyTable()

pt1.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Spouse"]
for person in people:
    pt1.add_row([person.id, person.name, person.gender, person.birthday, person.age, person.is_alive, person.death, person.spouse])
print(pt1)

pt2 = PrettyTable()
pt2.field_names = ["ID", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
for family in families:

    pt2.add_row([family.id, family.husband.id, family.husband.name, family.wife.id, family.wife.name, family.children])
print(pt2)