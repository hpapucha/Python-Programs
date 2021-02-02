
import unittest

class Student:
#__init__ method
    def __init__(self, username, last, first, phone, yr):
        self.username = username
        self.last = last
        self.first = first
        self.phone = phone
        self.yr = yr
        if self.yr < 1:
             self.yr == 1
        elif self.yr > 4:
             self.yr == 4
        elif self.yr <= 4 and self.yr >= 1:
             self.yr == yr
#__str__ method
    def __str__(self):
        return f"{self.username}, {self.last}, {self.first}, {self.phone}, {self.yr}"
#represent method
    def __repr__(self):
        return {self.username, self.last, self.first, self.phone, (self.yr)}
#update_year method
    def update_year(self):
        if self.yr < 4:
            return self.yr + 1


