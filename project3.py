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

for line in f.readlines():
    line = line.rstrip()

    line = line.split(' ', 2)
    person = None
    if len(line) > 2 and line[2] == 'INDI':
        id = line[1]
    if line[1] == 'NAME':
        name = line[2]
        name = name.replace('/', '')
        new_person = Person.Person()
        new_person.set_ID(id)
        new_person.set_name(name)
        people.append(new_person)

for person in people:
    print(person.id, person.name)

pt1 = PrettyTable()

pt1.field_names = ["ID, Name, Gender, Birthday, Age, Alive, Death, Child, Spouse"]
for person in people:
    pt1.add_row(person.id, person.name, person.gender, person.birthday, person.age, person.is_alive, person.death)

pt2 = PrettyTable()
pt2.field_names = ["ID, Married, Divorced, Husband ID, Husband Name, Wife ID, Wife Name, Children"]
