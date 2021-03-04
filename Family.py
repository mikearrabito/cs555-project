import Person


class Family:
    marriage = None
    children = list()

    def __init__(self, id):
        self.family_members = list()
        self.id = id

    def add_member(self, person):
        family_members.append(person)

    def add_marriage(self, partner_1, partner_2):
        self.marriage = (partner_1, partner_2)

    def add_child(self, child):
        children.append(child)

