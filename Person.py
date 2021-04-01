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

    def __str__(self):
        return self.id
    
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
                            
    """US07 Checks to make sure that an individual is less than 150 years old"""
    
    def age_less_than_150(individuals):

        flag = True
        output = ""
        for individual in individuals.values():
            if individual.alive:
    
                if individual.age > 150:
                    flag = False
                    output += "Error: " + \
                        str(individual.ID) + " is more than 150 years old.\n"
        if flag:
            output += "All individuals are less than 150 years old.\n"
        return (flag, output)
    
    
    """US08 Birth before marriage of parents"""
    
    def birth_before_marriage(individuals, families):
        for fam in families:
            wife = " ".join(families[fam]["WIFE"])
            husband = " ".join(families[fam]["HUSB"])
            if families[fam]["CHIL"] != []:
                children = families[fam]["CHIL"]
            else:
                continue
            for child in children:
                if individuals[child]["BIRT"] < families[fam]["MARR"]:
                    print(
                        "Error: US08: {} and {} married on {}, so {} cannot be born on {}".format(
                            husband,
                            wife,
                            families[fam]["MARR"].strftime("%Y-%m-%d"),
                            child,
                            individuals[child]["BIRT"].strftime("%Y-%m-%d"),
                        )
                    )
                if families[fam]["DIV"] != "" and individuals[child]["BIRT"] > families[fam]["DIV"] + datetime.timedelta(6 * 365 / 12):
                    print("Error: US08: {} and {} divorced on {}, so {} cannot be born on {}".format(
                            husband,
                            wife,
                            families[fam]["DIV"].strftime("%Y-%m-%d"),
                            child,
                            individuals[child]["BIRT"].strftime("%Y-%m-%d")))
        return True

    
    
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
                    self.divorce_date = date
                else:
                    self.divorce_date = 'Invalid date'
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
        
    def US_13(family_object, individual_object):
        """ To check if the sibiling are twins """
        warnings = set()
        for attribute in family_object.values():    
            child = list(attribute._children)
            if child != ['N','A']:
                for i in range(0, len(child)):          
                    for j in range(i + 1, len(child)):
                        person_one_id = child[i] 
                        person_two_id = child[j]

                        date_one = individual_object[person_one_id]._birth_date
                        date_two = individual_object[person_two_id]._birth_date
                        try:
                            difference = date_one - date_two
                        except:
                            continue
                        if date_one < date_two:
                            difference = date_two - date_one

                        if difference > datetime.timedelta(days=2) and difference < datetime.timedelta(days=240):
                            a = sorted([person_one_id, person_two_id])
                            warnings.add(f"The family id {attribute._family_id} has twins {individual_object[a[0]]._name} and {individual_object[a[1]]._name}, Line number: {attribute.get_line_numbers()['family_id']}")
            child = []       
        return warnings   
                             
    def US_14(individual, family):
        '''No more than five siblings should be born at the same time '''

        y = []
        b, n = 0, 0
        for k, v in family.items():
            # fam_result.extend(fam_result)
            child_bday = defaultdict(int)
            if len(v._children) >= 5:
                if v._children != 'NA':
                    for child in [individual[c] for c in v._children]:
                        child_bday[child._birth_date] += 1
                        for b_date, no in child_bday.items():
                            if no >= 5:
                                # y.append(b_date)
                                b = b_date
        if v._children != 'NA':
            output = f"US14: {k} has more than 5 children born on same date {b} in line number {family[k].get_line_numbers()['family_id']}"
            y.append(output)

        return y

    
    """US 15: Fewer than 15 siblings"""
    def fewerThanFifteen(families):
        for fam in families:
            if (len(families[fam]["CHIL"])>=15):
                print("Error: US15: Family {} cannot have 15 or more children.".format(fam))
        return True
    
    """US16"""
    def checkMaleLastNames(individuals):
        familyNames = {}
        for indi in individuals:
            if " ".join(individuals[indi]["SEX"]) == "F":
                continue
            lastName = individuals[indi]["NAME"][1][1:-1]
            if " ".join(individuals[indi]["FAMS"]) == "":
                family = " ".join(individuals[indi]["FAMC"])
            else:
                family = " ".join(individuals[indi]["FAMS"])
            try:
                if lastName == familyNames[family]:
                    continue
                else:
                    print(
                        "Error: US16: Last name of {} does not match family last name of {}".format(
                            indi, family
                        )
                    )
            except KeyError as ke:
                familyNames[family] = lastName
        return familyNames
    
    
    
    def set_is_child(self, is_child: bool):
        self.is_child = is_child
    
    def set_spouse(self, spouse):
        self.spouse.append(spouse)

    def set_fam(self, fam: str):
        self.child.append(fam)
    
