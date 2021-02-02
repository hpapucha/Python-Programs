

from random import shuffle
from card import Card

class Deck:

    # Initialize deck

    def __init__(self):
        self._cards = [ ]
        for suit in ["C", "D", "H", "S"]:
            for rank in range(2, 15):
                self._cards.append(Card(rank, suit))

    # Shows deck as a string object.	
    def __str__(self):
        output = ""
        counter = 1
        for card in self._cards:
            output += " " + str(card)
            if counter % 20 == 0:
                output += "\n"
            counter += 1
        return output
	
    # Gets rid oftop card from the deck and return
    def deal(self):
        return self._cards.pop( )

    # Puts a card to the top
    def add_to_top(self, the_card):
        self._cards.append(the_card)

    # Puts a card to the bottom
    def add_to_bottom(self, the_card):
        self._cards.insert(0, the_card)

    # Returs number of cards in deck
    def count(self):
        return len(self._cards)

     #Returns true if the deck is empty
    def is_empty(self):
        return len(self._cards) == 0

    # Shuffle method      
    def shuffle(self):
        shuffle(self._cards)

    
