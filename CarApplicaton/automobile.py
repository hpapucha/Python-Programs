# Automobile Example
# automobile.py file

class Automobile:

    def __init__(self, the_model, the_color):

        self.model = the_model
        self.color = the_color
        self.velocity = 0.0

    def __str__(self):
        return f"Model: {self.color} -- Color: {self.color}"

    def accelerate(self):
        self.velocity += 15
        if self.velocity > 120.0:
            self.velocity = 120.0

    def brake(self):
        self.velocity -= 20
        if self.velocity < 0.0:
            self.velocity = 0.0
