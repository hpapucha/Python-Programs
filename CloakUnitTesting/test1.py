from clock import Clock
import unittest


#first unit test
class MyUniTestClass(unittest.TestCase):
    def test_1(self):
        c = Clock(14, 23, 5)
        self.assertEqual(str(c), "14:23:05")
        self.assertEqual(c.hours, 14)
        self.assertEqual(c.minutes, 23)
        self.assertEqual(c.seconds, 5)
        c.tick()
        self.assertEqual(str(c), "14:23:06")
#second test minute change
    def test_2(self):
        c = Clock(4, 7, 59)
        self.assertEqual(str(c), "04:07:59")
        c.tick()
        self.assertEqual(str(c), "04:08:00")
#third test seconds change
    def test_3(self):
        c = Clock(4, 7, 3)
        self.assertEqual(str(c), "04:07:03")
        c.tick()
        self.assertEqual(str(c), "04:07:04")
#fourth test hour change, 23 hours to midnight
    def test_4(self):
        c = Clock(23, 59, 59)
        self.assertEqual(str(c), "23:59:59")
        c.tick()
        self.assertEqual(str(c), "00:00:00")
#fifth test hour change
    def test_5(self):
        c = Clock(10, 59, 59)
        self.assertEqual(str(c), "10:59:59")
        c.tick()
        self.assertEqual(str(c), "11:00:00")

    

if __name__ == '__main__':
    unittest.main()



