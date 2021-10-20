class PositiveReviewFinder:
    def __init__(self, reviews):
        self.reviews = reviews

    def find_overly_positive_reviews_based_on_number_of_exclamation_marks(self, number_of_reviews):
        self.reviews.sort(key=lambda r: r.count('!'))
        self.reviews.reverse()
        return self.reviews[:number_of_reviews]
