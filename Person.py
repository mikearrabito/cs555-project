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
            if birthday_date > self.death:
                self.birthday = 'Invalid date'
                return
        age = today.year - birthday_date.year 
        self.age = age
        
    """US05: Marriage should occur before death of either spouse"""

    def marriage_before_death(individual, family):
        for fam in family.values():
            married = fam._marriage_date
            for indi in individual.values():
                if fam._husband_id == indi._individual_id and indi._death_date != 'NA'and married!= "NA":
                    if indi._death_date < married:
                        yield f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}" \
                            f"\nDeath of Husband date Line: {indi._line_numbers.get('date').get('death')}\n" \
                            f"The family {fam._family_id} has a death of husband {fam._husband_id} before the marriage date."
                elif fam._wife_id == indi._individual_id and indi._death_date != 'NA' and married!= "NA":
                    if indi._death_date < married:
                        yield f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}" \
                            f"\nDeath of wife date Line: {indi._line_numbers.get('date').get('death')}\n" \
                            f"The family {fam._family_id} has a death of wife {fam._wife_id} before the marriage date."
                            
                            
    """ US06 : Divorce of the husband or wife must be before death date of the individual"""
                       
    def divorce_before_death(individual,family):
        lst = []
        for k, v in family.items():
            if v._divorce_date != 'NA':
                #get husband and wife ids death date
                husband_death = individual[v._husband_id]._death_date
                wife_death = individual[v._wife_id]._death_date

                if husband_death != 'NA' and husband_death < v._divorce_date:
                    lst.append(f"US_06: {v._husband_name} Death {husband_death} occured prior to the divorce date {v._divorce_date}")

                elif wife_death != 'NA' and wife_death < v._divorce_date:
                    lst.append(f"US_06: {v._wife_name} Death {wife_death} occured prior to the divorce date {v._divorced}")

        return lst
                            

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
        else:
            print(f"Error US02: Marriage date of {self.name} occurs before their birth date.")

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
    
