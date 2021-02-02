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


# Automobile Example
# test1.py file

from automobile import Automobile

auto = Automobile("Ford Taurus", "red")
print(str(auto))
# Next line has same effect as preceding line.
# str method is automatically called when
# an object printed.
print(auto)
print(auto.model, auto.color)

auto.accelerate( )
auto.accelerate( )
auto.accelerate( )
print(auto.velocity)

auto.brake( )
auto.brake( )
print(auto.velocity)

auto.brake( )
print(auto.velocity)
