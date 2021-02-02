


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        symbols = ["", "", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.rank == symbols
        return symbols[self.rank] + self.suit
    
    def color(self):
        if self.suit == "C" or self.suit == "S":
            return "black"
        else:
            return "red"


if __name__ == '__main__':
    unittest.main()
