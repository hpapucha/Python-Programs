from clock import Clock
import unittest

#Traditional test number 1
c1 = Clock(4, 7, 3)
print(c1)
print(c1.hours, c1.minutes, c1.seconds)
c1.tick( )
print(c1)
print("\n")
#Traditional test number 2 minutes change
c2 = Clock(4, 7, 59)
print(c2)
print(c2.hours, c2.minutes, c2.seconds)
c2.tick( )
print(c2)
print("\n")
#Traditional test number 3 hour change
c3 = Clock(4, 59, 59)
print(c3)
print(c3.hours, c3.minutes, c3.seconds)
c3.tick( )
print(c3)
print("\n")
#Traditional test number 4 day change
c4 = Clock(23, 59, 59)
print(c4)
print(c4.hours, c4.minutes, c4.seconds)
c4.tick( )
print(c4)
