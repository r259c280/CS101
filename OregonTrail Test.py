import unittest
import OregonTrailKey as ot

class PersonTest(unittest.TestCase):

    def test_something(self):

            person = ot.person("Name1")
            self.assertIsInstance(person, ot.Person)

    def test_str(self):

            person = ot.person("Bob")
            p_str = str(person)
            self.assertEqual(p_str, "Bob - 100")

unittest.man()
