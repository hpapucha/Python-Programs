

from card   import Card
from pokerhand import PokerHand
from constants import *
import unittest

class MyUnitTestClass(unittest.TestCase):
#STRAIGHT FLUSH TEST
    
    def test_straight_flush(self):
        arr =  [ Card(8, "C"), Card(9, "C"),
                 Card(10, "C"), Card(11, "C"),
                 Card(12, "C") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, STRAIGHT_FLUSH)
        
#FOUR OF A KIND TEST
        
    def test_four_of_kind(self):

        arr =  [ Card(9, "C"), Card(9, "S"),
                 Card(9, "H"), Card(9, "D"),
                 Card(11, "S") ]
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FOUR_OF_A_KIND)

        arr = [ Card(3, "S"), Card(13, "C"), 
                Card(13, "S"), Card(13, "H"), 
                Card(13, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FOUR_OF_A_KIND)
        
#FULL HOUSE TEST

    def test_full_house(self):
        arr =  [ Card(2, "C"), Card(2, "S"),
                 Card(2, "H"), Card(12, "C"),
                 Card(12, "D") ]

        arr =  [ Card(2, "C"), Card(2, "S"),
                 Card(12, "H"), Card(12, "C"),
                 Card(12, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FULL_HOUSE)



#FLUSH TEST
        
        
    def test_flush(self):
        arr =  [ Card(6, "C"), Card(7, "C"),
                 Card(10, "C"), Card(12, "C"),
                 Card(3, "C") ]

        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, FLUSH)
        


#STRAIGHT TEST
    def test_straight(self):
        arr = [Card(6, "D"), Card(7, "C"),
               Card(8, "H"), Card(9, "C"),
               Card(10, "C") ]

        ph = PokerHand(arr)
        ph.classify()
        self.assertEqual(ph.hand_type, STRAIGHT)


#THREE OF A KIND TEST        
    def test_three_of_a_kind(self):
        arr =  [ Card(6, "D"), Card(6, "S"),
                 Card(6, "C"), Card(2, "H"),
                 Card(3, "C") ]

        arr =  [ Card(9, "D"), Card(6, "S"),
                 Card(7, "C"), Card(7, "H"),
                 Card(7, "D") ]

        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, THREE_OF_A_KIND)

#TWO PAIR TEST    
    def test_two_pair(self):
        arr =  [ Card(2, "D"), Card(2, "S"),
                 Card(7, "C"), Card(7, "H"),
                 Card(3, "D") ]

    def test_two_pair(self):
        arr =  [ Card(9, "D"), Card(9, "S"),
                 Card(7, "C"), Card(10, "H"),
                 Card(10, "D") ]

    def test_two_pair(self):
        arr =  [ Card(11, "D"), Card(4, "S"),
                 Card(4, "C"), Card(1, "H"),
                 Card(1, "D") ]

        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, TWO_PAIR)
        
#ONE PAIR TEST
    def test_one_pair(self):
        arr =  [ Card(2, "D"), Card(2, "S"),
                 Card(10, "C"), Card(3, "H"),
                 Card(9, "D") ]

    def test_one_pair(self):
        arr =  [ Card(3, "D"), Card(2, "S"),
                 Card(2, "C"), Card(10, "H"),
                 Card(9, "D") ]

    def test_one_pair(self):
        arr =  [ Card(2, "D"), Card(9, "S"),
                 Card(2, "C"), Card(2, "H"),
                 Card(8, "D") ]

    def test_one_pair(self):
        arr =  [ Card(11, "D"), Card(3, "S"),
                 Card(10, "C"), Card(2, "H"),
                 Card(2, "D") ]
        
        ph = PokerHand(arr)
        ph.classify( )
        self.assertEqual(ph.hand_type, ONE_PAIR)      

if __name__ == '__main__':
    unittest.main( )
