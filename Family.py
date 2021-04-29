import Person
from dateutil.relativedelta import relativedelta
import datetime

class Family:
  

    def __init__(self, id):
        self.family_members = list()
        self.id = id
        self.children = list()
        self.husband = None
        self.wife = None
        self.family_members = list()
        self.divorced = False
        self.marriage_date = None

    def add_member(self, person):
        self.family_members.append(person)

    def get_children_ids(self):
        ids = list()
        for child in self.children:
            ids.append(child.id)
        return ids

    def add_husband(self, husband):
        self.husband = husband

    def add_wife(self, wife):
        self.wife = wife

    def add_child(self, child):
        """US 12 Mother should be less than 60 years older than her children and
                 father should be less than 80 years older than his children"""
        mother_limit = None
        father_limit = None
        if wife.age:
            mother_limit = wife.age
        if father.age:
            father_limit = father.age
        if mother_limit:
            if child.age and (mother_limit - 60) > child.age:
                print("Mother is too old to add this child")
                return
        if father_limit:
            if child.age and (father_limit - 80) > child.age:
                print("Father is too old to add this child")
                return
        self.children.append(child)
        

    def set_marriage_date(self, date):
        self.marriage_date = date

    def set_divorced_date(self, date):
        self.divorced_date = date

    
    def is_birth_before_death_of_parents(self):
        for child in self.children:
            if not (self.wife.death == "N/A"):
                if datetime.datetime.strptime(child.birthday, "%d %b %Y") > datetime.datetime.strptime(self.wife.death, "%d %b %Y"):
                    print(f"Error US09: Death date of {self.wife.name} occurs before {child.name} birth date.")
                    return False
            if not (self.husband.death == "N/A"):
                birthday = datetime.datetime.strptime(child.birthday, "%d %b %Y") - relativedelta(months=+9)
                if birthday > datetime.datetime.strptime(self.husband.death, "%d %b %Y"):
                    print(f"Error US09: Birth date of {child.name} occurs before 9 months after {self.husband.name} death date.")
                    return False
        return True

    def is_marriage_fourteen_years_after_parents_birth(self):
        if self.marriage_date == None:
            return True
        marriage_date = datetime.datetime.strptime(self.marriage_date, "%d %b %Y") - relativedelta(years=+14)
        if datetime.datetime.strptime(self.husband.birthday, "%d %b %Y") > marriage_date:
            print(f"Error US10: {self.husband.name} is not at least 14 years old at time of marriage")
            return False
        if datetime.datetime.strptime(self.wife.birthday, "%d %b %Y") > marriage_date:
            print(f"Error US10: {self.wife.name} is not at least 14 years old at time of marriage")
            return False
        return True

    def children_married_to_each_other(self):
        for child in self.children:
            for other in self.children:
                if child.spouse == other.id:
                    print(f"Error US18: {child} is married to sibling {other}")
                    return True
        return False
        
    def parents_married_to_children(self):
        for child in self.children:
            if self.husband.spouse == child.id:
                print(f"Error US17: {self.husband} is married to child {child}")
                return True
            if self.wife.spouse == child.id:
                print(f"Error US17: {self.wife} is married to child {child}")
                return True
        return False

    def kids_have_same_name(self):
        same_name = 0

        for child in self.children:
            for child1 in self.children:
                if child.name == child1.name and child.birthday == child1.birthday:
                    same_name += 1
            if same_name >= 2:
                print(f"Error US25: Two kids with the same name and birthdate.")
                return False
            same_name = 0
        
        return True

    