from Person import Person
import unittest

class PersonTest(unittest.TestCase):

    def test_is_date_valid(self) -> None:
        self.assertTrue(Person.is_date_valid("3 MAR 2021"))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)