import unittest
from score import score_completion


class TestScoring(unittest.TestCase):

    def test_scoring_normal(self):
        self.assertEqual(16, score_completion("to be or", "to be or"))

    def test_scoring_extra(self):
        self.assertEqual(14, score_completion("to be orr", "to be or"))
        self.assertEqual(10, score_completion("too be or", "to be or"))

    def test_scoring_missing(self):
        self.assertEqual(6, score_completion("t be or", "to be or"))
        self.assertEqual(12, score_completion("to beor", "to be or"))

    def test_scoring_diff(self):
        self.assertEqual(13, score_completion("to be ot", "to be or"))
        self.assertEqual(10, score_completion("ta be or", "to be or"))


if __name__ == '__main__':
    unittest.main()
