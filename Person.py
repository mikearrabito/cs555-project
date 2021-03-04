import datetime

class Person:
    

    def __init__(self):
        self.is_alive = True
        self.death = "N/A"
        self.spouse = []
        self.child = []
    
    def set_ID(self, id: str):
        self.id = id
    
    def set_name(self, name: str):
        self.name = name

    def set_gender(self, gender: str):
        self.gender = gender

    def set_birthday(self, birthday: str):
        self.birthday = birthday
        today = datetime.date.today()
        birthday_date = datetime.datetime.strptime(birthday, "%d %b %Y")
        age = today.year - birthday_date.year 
        self.age = age
    
    def set_death(self, death: str):
        self.death = death
        self.is_alive = False
    
    def set_is_child(self, is_child: bool):
        self.is_child = is_child
    
    def set_spouse(self, spouse):
        self.spouse.append(spouse)

    def set_fam(self, fam: str):
        self.child.append(fam)
    