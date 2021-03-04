from datetime import date

class Person:

    def __init__(self):
        pass
    
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

    def set_is_alive(self, is_alive: bool):
        self.is_alive = is_alive
    
    def set_death(self, death: str):
        self.death = death
    
    def set_is_child(self, is_child: bool):
        self.is_child = is_child
    
    def set_is_spouse(self, is_spouse):
        self.is_spouse = is_spouse

    def set_fam(self, fam: str):
        self.fam = fam
    