

from student import Student
#Traditional testing method

#Constructor method
s = Student(111, "Carter", "Marilyn", "312/333/2222", 1)
print(s)
#__repr__ method
s = Student(112, "Snow", "Jon", "312/2222/2222", 2)
#Testing instanced members
print(s.__repr__())
print(s.username)
print(s.first)
print(s.last)
print(s.phone)
print(s.yr)
#update_year for "s = Student(112, "Snow", "Jon", "312/2222/2222", 2)"
#updates by +1
print(s.update_year())

