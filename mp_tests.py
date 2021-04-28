from Person import Person
import unittest
from Family import Family

class PersonTest(unittest.TestCase):

    def test_is_date_valid(self):
        self.assertTrue(Person.is_date_valid("3 MAR 2021"))

    def test_birth_before_death(self):
        person1 = Person()
        person1.set_birthday("10 JUN 2020")
        person1.set_death("10 MAY 2020")
        self.assertEqual(person1.death, 'N/A')
        return

    def test_marriage_before_divorce(self):
        person1 = Person()
        person1.set_birthday("1 JAN 1997")
        person1.set_marriage_date("10 MAY 2020")
        person1.set_divorce_date("10 JUN 2020")
        self.assertEqual(person1.divorce_date, "10 JUN 2020")
        person1.set_divorce_date("10 APR 2020")
        self.assertEqual(person1.divorce_date, "Invalid date")
        return

    def test_is_birth_before_death_of_parents(self):
        wife = Person()
        wife.set_birthday("1 JAN 1910")
        wife.name = "Kim"
        wife.set_death("16 MAR 1952")
        child = Person()
        child.name = "Sally"
        child.set_birthday("17 MAR 1952")
        family = Family("1")
        family.wife = wife
        family.add_child(child)
        self.assertFalse(family.is_birth_before_death_of_parents())
        husband = Person()
        husband.set_birthday("1 JAN 1910")
        husband.name = "Joe"
        husband.set_death("5 JAN 1952")
        family.add_husband(husband)
        family.wife.set_death("10 MAR 1970")
        self.assertTrue(family.is_birth_before_death_of_parents())
        family.husband.set_death("5 APR 1951")
        self.assertFalse(family.is_birth_before_death_of_parents())

    def test_is_marriage_fourteen_years_after_parents_birth(self):
        wife = Person()
        wife.set_birthday("1 JAN 1910")
        wife.name = "Kim"
        husband = Person()
        husband.set_birthday("1 JAN 1910")
        husband.name = "Joe"
        family = Family("1")
        family.husband = husband
        family.wife = wife
        family.set_marriage_date("1 JAN 1923")
        self.assertFalse(family.is_marriage_fourteen_years_after_parents_birth())
        family.set_marriage_date("1 JAN 1925")
        self.assertTrue(family.is_marriage_fourteen_years_after_parents_birth())

    def test_children_married_to_each_other(self):
        kid1 = Person()
        kid1.id = "@02@"
        kid1.spouse = "@01@"
        kid2 = Person()
        kid2.id = "@01@"
        family = Family("@f1@")
        family.add_child(kid1)
        family.add_child(kid2)
        self.assertTrue(family.children_married_to_each_other())
        kid1.spouse = "@05@"
        self.assertFalse(family.children_married_to_each_other())

    def test_parents_married_to_children(self):
        kid1 = Person()
        kid1.set_ID("@02@")
        kid1.spouse = "@01@"
        family = Family("@f1@")
        family.add_child(kid1)
        wife = Person()
        wife.spouse= "@02@"
        wife.set_ID("05")
        family.wife = wife
        husband = Person()
        husband.set_spouse("05")
        family.husband = husband
        self.assertTrue(family.parents_married_to_children())

    def test_kids_have_same_name(self):
        kid1 = Person()
        kid1.set_name("Joe")
        kid1.set_birthday("1 JAN 1923")
        kid2 = Person()
        kid2.set_name("Joe")
        kid2.set_birthday("1 JAN 1923")
        family = Family("id")
        family.add_child(kid1)
        family.add_child(kid2)
        self.assertFalse(family.kids_have_same_name())
        kid2.name = "Bill"
        self.assertTrue(family.kids_have_same_name())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)