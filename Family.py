import Person


class Family:
    def __init__(self, id):
        self.family_members = list()
        self.id = id
        
    def add_member(self, Person):
        self.family_members.append(Person)

