import datetime

class Person:
    

    def __init__(self):
        self.is_alive = True
        self.birthday = None
        self.death = "N/A"
        self.spouse = []
        self.child = []
        self.divorce_date = None
        self.marriage_date = None
    
    #returns True if date is before today
    @staticmethod
    def is_date_valid(date: str):

        date1 = datetime.datetime.strptime(date, "%d %b %Y")
        today = datetime.datetime.today().date()
        #today = datetime.date.today().strftime("%d %b %Y")
        if date1.date() < today:
            return True
        else:
            return False
        
    

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
        if self.death != 'N/A':
            # if person is dead, make sure dob is not after death date
            if self.birthday_date > self.death:
                self.birthday = 'Invalid date'
                return
        age = today.year - birthday_date.year 
        self.age = age
    
    def set_marriage_date(self, date: str):
        if datetime.datetime.strptime(date, "%d %b %Y") > datetime.datetime.strptime(self.birthday, "%d %b %Y"):
            if self.divorce_date:
                if datetime.datetime.strptime(date, "%d %b %Y") < datetime.datetime.strptime(self.divorce_date,
                                                                                             "%d %b %Y"):
                    # check if marriage date is before divorce date if we have already added that
                    self.marriage_date = date
            else:
                # divorce date not added yet, so add marriage date
                self.marriage_date = date

    def set_divorce_date(self, date: str):
        if datetime.datetime.strptime(date, "%d %b %Y") > datetime.datetime.strptime(self.birthday, "%d %b %Y"):
            if self.marriage_date:
                if datetime.datetime.strptime(date, "%d %b %Y") > datetime.datetime.strptime(self.marriage_date,
                                                                                             "%d %b %Y"):
                    # check if divorce date is after marriage date
                    self.marriage_date = date
            else:
                # marriage date not added yet, so add divorce date
                self.divorce_date = date


    def set_death(self, date: str):
        # if death is before date of birth, then we have an invalid death date
        if datetime.datetime.strptime(date, "%d %b %Y") > datetime.datetime.strptime(self.birthday, "%d %b %Y"):
            self.death = date
            self.is_alive = False
        else:
            pass  # death is before date of birth

    
    def set_is_child(self, is_child: bool):
        self.is_child = is_child
    
    def set_spouse(self, spouse):
        self.spouse.append(spouse)

    def set_fam(self, fam: str):
        self.child.append(fam)
    