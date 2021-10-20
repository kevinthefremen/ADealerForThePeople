import unittest

from requests.exceptions import MissingSchema

from src import ReviewScraper, scrape_page_for_paragraph_text_by_class


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer" \
                        "-reviews-23685"
        self.review_scraper = ReviewScraper(self.base_url)

    def test_scrape_page_gets_review_text(self):
        reviews_text = scrape_page_for_paragraph_text_by_class(self.base_url, "review-content")

        self.assertEqual(len(reviews_text), 10)
        self.assertTrue(type(reviews_text[0]) is str)

    def test_scrape_invlaid_url(self):
        self.assertRaises(MissingSchema,
                          lambda: scrape_page_for_paragraph_text_by_class("invalidurl.com", "no-content"))

    def test_scrape_invalid_content_returns_empty_list(self):
        result = scrape_page_for_paragraph_text_by_class(self.base_url, "invalid-content")

        self.assertEqual(len(result), 0)

    def test_scrape_pages_gets_all_reviews_from_all_pages(self):
        reviews = self.review_scraper.scrape_pages_for_reviews(5)

        self.assertEqual(len(reviews), 50)


if __name__ == '__main__':
    unittest.main()
