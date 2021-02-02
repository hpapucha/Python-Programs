

#Unit testing
import unittest
from student import Student

class MyTest(unittest.TestCase):
    def test_1(self):
#Testing __str__
        s = Student("111", "Carter", "Marilyn", "312/333/2222", 1)
        self.assertEqual(str(s), "111, Carter, Marilyn, 312/333/2222, 1")
#Testing __repr__
        s = Student(112, "Snow", "Jon", "312/2222/2222", 2)
        c = s.__repr__()
        self.assertEqual(c, {2, 112, '312/2222/2222', 'Snow', 'Jon'})
#Testing instanced members
        s = Student(112, "Snow", "Jon", "312/2222/2222", 2)
        self.assertEqual(s.username, 112)
        self.assertEqual(s.last, "Snow")
        self.assertEqual(s.first, "Jon")
        self.assertEqual(s.phone, "312/2222/2222")
        self.assertEqual(s.yr, 2)
#Update_year method
        s = Student(112, "Snow", "Jon", "312/2222/2222", 1)
        c = s.update_year()
        self.assertEqual(s.update_year(), 2)
        s = Student(112, "Snow", "Jon", "312/2222/2222", 2)
        c = s.update_year()
        self.assertEqual(s.update_year(), 3)





if __name__ == '__main__':
    unittest.main()
