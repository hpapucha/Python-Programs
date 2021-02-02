class Card:

#Init method
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

#Colors method
    def color(self):
        if (self.suit == "C" or self.suit =="S"):
            return "black"
        else:
            return "red"
        
#Str method
    def __str__(self):
        symbols = ["", "", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "J", "Q", "K", "A"]
        return symbols[self.rank] + self.suit
#Represent method
    def __repr__(self):
        return str(self)
#Less than method        
    def __lt__(self, other):
        return self.rank < other.rank
#Equal method
    def __eq__(self, other):
        return self.rank == other.rank
