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

__str__
