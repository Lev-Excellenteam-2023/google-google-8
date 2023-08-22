import unittest
import search_words
import insertion


class TestCalculations(unittest.TestCase):

    # def setUp(self):
    #     self.calculation = Calculations(8, 2)

    def test_finding_follower_number(self):
        self.assertEqual(search_wards.finding_follower_number(7, [1, 8, 13]), 8)
        self.assertEqual(search_wards.finding_follower_number(7, [1, 9, 13]), -1)
        self.assertEqual(search_wards.finding_follower_number(7, []), -1)

    def test_search_word_in_tree(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.search_word_in_tree("home"), {2: [3], 3: [1, 8], 4: [1], 5: [1], 6: [3], 7: [1]})
        self.assertEqual(search_wards.search_word_in_tree("h"), {})

    def test_search_word_in_tree(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.search_suggestion(["home", "documentation"]), [2, 3, 4, 5, 6, 7])
        self.assertEqual(search_wards.search_suggestion(["home", "doc"]), [])

    def test_find_in_dict(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.find_in_dict(2),
                         insertion.SentenceInfo(sentence='Bitbucket Server documentation home documentation \n',
                                                source='C:\\networks\\google8\\google-google-8\\Archive1\\dsfd.txt',
                                                offset=1))
        self.assertEqual(search_wards.find_in_dict(10), None)
        self.assertEqual(search_wards.find_in_dict("dd"), None)
        self.assertEqual(search_wards.find_in_dict("1"), None)

    def test_correction_to_input(self):
        search_wards.init_system("C:\\networks\\google8\\google-google-8\\Archive1")
        self.assertEqual(search_wards.correction_to_input(["bome", "documentation"]),
                         {'home documentation': [2, 3, 4, 5, 6, 7], 'vome documentation': [8]})
        self.assertEqual(search_wards.correction_to_input(["ome", "documentation"]),
                         {'home documentation': [2, 3, 4, 5, 6, 7], 'vome documentation': [8]})
        self.assertEqual(search_wards.correction_to_input(["bomke", "documentation"]), {})
        self.assertEqual(search_wards.correction_to_input(["hdome", "documentation"]),
                         {'home documentation': [2, 3, 4, 5, 6, 7]})

    def test_correction_to_input(self):
        search_wards.init_system(r"C:\Users\tamar\excellenteam\bootcamp\googleProj\project\Archive-test\temp")
        pass

    def test_get_word_corrections(self):
        search_wards.init_system(r"C:\Users\tamar\excellenteam\bootcamp\googleProj\project\Archive-test\temp")
        possible_results = set(
            [
                'cat',
                'xar',
                'cart',
                'ar',
                'car']
        )
        self.assertEqual(possible_results, set(search_wards.get_word_corrections('car')))

    def test_get_best_k_completions(self):
        search_wards.init_system(r"C:\Users\tamar\excellenteam\bootcamp\googleProj\project\Archive-test\temp")
        expected = set(
            ['Bitbucket Server car documentation home documentation\n',
             'documentation home documentation cat of the Getting started documentation home\n',
             'documentation home cart documentation\n',
             'ggg gg documentation xar home documentation\n',
             'nj car hello world\n'
             ]
        )
        actual = [sentence.completed_sentence for sentence in search_wards.get_best_k_completions('car')]
        self.assertEqual(expected, set(actual))


if __name__ == '__main__':
    unittest.main()
