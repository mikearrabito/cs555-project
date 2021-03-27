import Person


class Family:
  

    def __init__(self, id):
        self.family_members = list()
        self.id = id
        self.children = list()
        self.husband = None
        self.wife = None
        self.family_members = list()
        self.divorced = False

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
        self.children.append(child)
        

    def set_marriage_date(self, date):
        self.marriage_date = date

    def set_divorced_date(self, date):
        self.divorced_date = date

