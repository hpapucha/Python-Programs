

from deck import Deck
#from card import Card
import unittest

#Testing the Card method
class MyTest(unittest.TestCase):
#Self assert method


    def test_3(self):
#Deal Method
        d = Deck( )
        c = d.deal( )
        self.assertEqual(str(c), "AS")
        self.assertEqual(d.count( ), 51)
        print(d.count( ))
#Add to top method
    def test_4(self):
        d = Deck( )
        c = d.add_to_top("JS")
        self.assertEqual(d.count(),53)
#Add to bottom method
    def test_5(self):
        d = Deck( )
        c = d.add_to_bottom("JH")
        self.assertEqual(d.count( ), 53)
#Count method
    def test_6(self):
        d = Deck( )
        c = d.count( )
        self.assertEqual(d.count( ), 52)
#Is Empty method
    def test_7(self):
        d = Deck( )
        c = d.is_empty( )
        self.assertEqual(d.is_empty( ), False)
#Constructor method
    def test_8(self):
        d = Deck( )
        c = d.__init__()
        self.assertEqual(" ", " ")

        
        

#Unit test
if __name__ == '__main__':
    unittest.main( )




