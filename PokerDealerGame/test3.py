

from card import Card
from deck import Deck
from constants import *
from pokerhand import PokerHand

#Create array named counts
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(0, 2000):
    deck = Deck( )
    deck.shuffle( )
    poker_hands = [ ]

    for i in range(0,5):
        arr = [ ]
        for j in range (0,5):
            arr.append(deck.deal( ))
        
        ph = PokerHand(arr)
        poker_hands.append(ph)
         
    for ph in poker_hands:
        ph.classify()
      
    for ph in poker_hands:
        counts[ph.hand_type] += 1
#Print array named counts   
print(counts)
