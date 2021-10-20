import unittest
from src import PositiveReviewFinder


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.positive_review_finder = PositiveReviewFinder(["review!", "review!!", "review", "review!!!!!"])

    def test_find_one(self):
        result = self.positive_review_finder.find_overly_positive_reviews_based_on_number_of_exclamation_marks(1)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "review!!!!!")

    def test_find_top_two(self):
        result = self.positive_review_finder.find_overly_positive_reviews_based_on_number_of_exclamation_marks(2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "review!!!!!")
        self.assertEqual(result[1], "review!!")

    def test_find_all_sorted_by_positivity(self):
        result = self.positive_review_finder.find_overly_positive_reviews_based_on_number_of_exclamation_marks(4)

        self.assertEqual(len(result), 4)
        self.assertEqual(result, ["review!!!!!", "review!!", "review!", "review"])


if __name__ == '__main__':
    unittest.main()
