
import random
from card import Card
from deck import Deck

#Traditional testing method card/suite

#Note: These tests execute in order

#add_to_top method, add a card to the top
d = Deck ()
c = Card(12, "S")
d.add_to_top(c)
print(d)
print("\n")
#add_to_bottom method, add a card to the bottom
d = Deck ()
c = Card(11, "D")
d.add_to_bottom(c)
print(d)
print("\n")
#Deal method, remove the top card 
d = Deck ()
d.deal()
print(d)
print("\n")
#Count method
print(d.count( ))
print( )
print("\n")
#is_empty method, checks if the deck is empty and returns a bool
d = Deck ()
d.is_empty()
print(d.is_empty())
print("\n")
#__str__ method, testing
d = Deck ()
d.__str__()
print(d.__str__())
print("\n")
#Shuffle method
d.shuffle()
print(d)
print("\n")
#__init__ method
d = Deck ()
d.__init__()
print(d.__init__())




