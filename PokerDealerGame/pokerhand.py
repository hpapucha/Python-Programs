

from card import Card
from deck import Deck
from constants import *



# Creates PokerHand Class
class PokerHand:

    def __init__(self, the_array): # Method 
        self._cards = [ ]
        for c in the_array:
            self._cards.append(c)
        
    def classify(self):
        self._cards.sort( )

    # STRAIGHT FLUSH CLASS
        if self._cards[0].rank + 1 == self._cards[1].rank and \
           self._cards[1].rank + 1 == self._cards[2].rank and \
           self._cards[2].rank + 1 == self._cards[3].rank and \
           self._cards[3].rank + 1 == self._cards[4].rank and \
           self._cards[0].suit == self._cards[1].suit     and \
           self._cards[1].suit == self._cards[2].suit     and \
           self._cards[2].suit == self._cards[3].suit     and \
           self._cards[3].suit == self._cards[4].suit:
       
                self.hand_type = STRAIGHT_FLUSH
                
    # FOUR OF A KIND PAIR CLASS
        elif self._cards[0] == self._cards[1] and \
             self._cards[1] == self._cards[2] and \
             self._cards[2] == self._cards[3]:

                self.hand_type = FOUR_OF_A_KIND

        elif self._cards[1] == self._cards[2] and \
             self._cards[2] == self._cards[3] and \
             self._cards[3] == self._cards[4]:

                self.hand_type = FOUR_OF_A_KIND
        
    # FULL HOUSE CLASS
        elif self._cards[0] == self._cards[1] and \
             self._cards[1] == self._cards[2] and \
             self._cards[3] == self._cards[4]:
            
                self.hand_type = FULL_HOUSE
    
        elif self._cards[0] == self._cards[1] and \
             self._cards[2] == self._cards[3] and \
             self._cards[3] == self._cards[4]:
            
                self.hand_type = FULL_HOUSE
    
    # FLUSH CLASS
        elif self._cards[0].suit == self._cards[1].suit and \
           self._cards[1].suit == self._cards[2].suit   and \
           self._cards[2].suit == self._cards[3].suit   and \
           self._cards[3].suit == self._cards[4].suit:
       
                self.hand_type = FLUSH

    # STRAIGHT CLASS
        elif self._cards[0].rank + 1 == self._cards[1].rank and \
             self._cards[1].rank + 1 == self._cards[2].rank and \
             self._cards[2].rank + 1 == self._cards[3].rank and \
             self._cards[3].rank + 1 == self._cards[4].rank:

                self.hand_type = STRAIGHT

     # THREE OF A KIND CLASS
        elif self._cards[0] == self._cards[1] and \
             self._cards[1] == self._cards[2]:
        
                self.hand_type = THREE_OF_A_KIND

        elif self._cards[1] == self._cards[2] and \
             self._cards[2] == self._cards[3]:
                
                self.hand_type = THREE_OF_A_KIND

        elif self._cards[2] == self._cards[3] and \
             self._cards[3] == self._cards[4]:
                
                self.hand_type = THREE_OF_A_KIND
            
    # TWO PAIR CLASS
        elif self._cards[0] == self._cards[1] and \
             self._cards[2] == self._cards[3] :
        
                self.hand_type = TWO_PAIR
                
        elif self._cards[0] == self._cards[1] and \
             self._cards[3] == self._cards[4] :
        
                self.hand_type = TWO_PAIR

        elif self._cards[1] == self._cards[2] and \
             self._cards[3] == self._cards[4]:

                self.hand_type = TWO_PAIR

    # ONE PAIR CLASS
        elif self._cards[0] == self._cards[1]:
            
                self.hand_type = ONE_PAIR
                
        elif self._cards[1] == self._cards[2]:
            
                self.hand_type = ONE_PAIR
                
        elif self._cards[2] == self._cards[3]:
            
                self.hand_type = ONE_PAIR

        elif self._cards[3] == self._cards[4]:
            
                self.hand_type = ONE_PAIR
    #NO PAIR CLASS
        else:
            self.hand_type = NO_PAIR
