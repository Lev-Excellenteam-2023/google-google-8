import unittest
import search_wards
class TestCalculations(unittest.TestCase):

    # def setUp(self):
    #     self.calculation = Calculations(8, 2)

    def test_finding_follower_number(self):
        self.assertEqual(search_wards.finding_follower_number(7,[1,8,13]), 8)
        self.assertEqual(search_wards.finding_follower_number(7,[1,9,13]), -1)
        self.assertEqual(search_wards.finding_follower_number(7,[]), -1)



if __name__ == '__main__':
    unittest.main()