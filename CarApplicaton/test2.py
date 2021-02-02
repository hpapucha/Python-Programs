# Automobile Example
# test2.py file

from automobile import Automobile

herbie = Automobile("VW Bug", "yellow")
christine = Automobile("Plymouth Fury", "red")

print(christine.color)
herbie.color = "white"

for i in range(0, 5):
    herbie.accelerate( )
    christine.accelerate( )
    print("herbie", herbie.velocity)
print("christine", christine.velocity)

for i in range(0, 3):
    herbie.brake( )

print(christine.velocity, herbie.velocity)
print(herbie)
print(christine)
