import unittest
from minNumOfBananasPerHour import min_Num_Of_Bananas_Per_Hour

class TestEatBananas(unittest.TestCase):
    def test_1(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(min_Num_Of_Bananas_Per_Hour(piles, H), 4)

    def test_2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(min_Num_Of_Bananas_Per_Hour(piles, H), 30)

    def test_3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(min_Num_Of_Bananas_Per_Hour(piles, H), 23)
    

if __name__ == '__main__':
    unittest.main()
