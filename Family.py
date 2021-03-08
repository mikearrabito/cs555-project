import Person


class Family:
    husband = None
    wife = None
    children = list()
    family_members = list()
    divorced = False

    def __init__(self, id):
        self.family_members = list()
        self.id = id

    def add_member(self, person):
        self.family_members.append(person)


    def add_husband(self, husband):
        self.husband = husband

    def add_wife(self, wife):
        self.wife = wife

    def add_child(self, child):
        self.children.append(child)

