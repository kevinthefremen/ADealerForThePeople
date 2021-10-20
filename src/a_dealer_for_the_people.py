from website_scraper import ReviewScraper
from positive_review_finder import PositiveReviewFinder


def main():
    base_url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685"
    pages_to_scrape = 5
    reviews = scrape_for_reviews(base_url, pages_to_scrape)
    overly_positive_reviews = identify_overly_positive_reviews(reviews)
    message = f'''The following reviews present a risk for project McKaig Chevrolet Buick: A Dealer For The People. 
These reviews should be removed immediately.
    1. "{overly_positive_reviews[0]}"
    2. "{overly_positive_reviews[1]}"
    3. "{overly_positive_reviews[2]}"'''
    print(message)


def identify_overly_positive_reviews(reviews):
    positive_review_finder = PositiveReviewFinder(reviews)
    number_of_reviews_to_flag = 3
    overly_positive_reviews = positive_review_finder.find_overly_positive_reviews_based_on_number_of_exclamation_marks(number_of_reviews_to_flag)
    return overly_positive_reviews


def scrape_for_reviews(base_url, pages_to_scrape):
    website_review_scraper = ReviewScraper(base_url)
    reviews = website_review_scraper.scrape_pages_for_reviews(pages_to_scrape)
    if len(reviews) == 0:
        print(f'It appears there are no reviews. Please verify the dealership URL: {base_url}')
    return reviews


if __name__ == '__main__':
    main()
