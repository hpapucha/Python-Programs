

from card import Card
import unittest

class MyUnitTestClass(unittest.TestCase):
#Cards are 8 of spades, Queen of clubs, 8 of spades
    def test_1(self):
        c1 = Card(8, "S")
        c2 = Card(12, "C")
        c3 = Card(8, "C")

     # __lt__ test method
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c1 > c3, False)

    # __eq__ test method
        self.assertEqual(c1 == c2, False)
        self.assertEqual(c1 == c3, True)

if __name__ == '__main__':
    unittest.main( )
