from Person import Person
import unittest

class PersonTest(unittest.TestCase):

    def test_is_date_valid(self) -> None:
        self.assertTrue(Person.is_date_valid("3 MAR 2021"))

    def test_birth_before_death(self):
        person1 = Person()
        person1.set_death("10 MAY 2020")
        person1.set_birthday("10 JUN 2020")
        self.assertEquals(person1.birthday, 'Invalid date')
        return

    def test_marriage_before_divorce(self):
        person1 = Person()
        person1.set_marriage_date("10 MAY 2020")
        person1.set_divorce_date("10 JUN 2020")
        self.assertEquals(person1.divorce_date, "10 JUN 2020")
        person1.set_divorce_date("10 APR 2020")
        self.assertEquals(person1.divorce_date, "Invalid date")
        return


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)