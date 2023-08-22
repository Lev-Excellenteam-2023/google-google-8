import unittest
import search_wards
from unittest.mock import Mock


class TestCalculations(unittest.TestCase):

    # def setUp(self):
    #     self.calculation = Calculations(8, 2)


    def test_finding_follower_number(self):
        self.assertEqual(search_wards.finding_follower_number(7,[1,8,13]), 8)
        self.assertEqual(search_wards.finding_follower_number(7,[1,9,13]), -1)
        self.assertEqual(search_wards.finding_follower_number(7,[]), -1)

    def test_search_word_in_tree(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.search_word_in_tree("home"),{2: [3], 3: [1, 8], 4: [1], 5: [1], 6: [3], 7: [1]})
        self.assertEqual(search_wards.search_word_in_tree("h"),{})

    def test_search_word_in_tree(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.search_suggestion(["home", "documentation"]),[2, 3, 4, 5, 6, 7])
        self.assertEqual(search_wards.search_suggestion(["home", "doc"]),[])




if __name__ == '__main__':
    unittest.main()