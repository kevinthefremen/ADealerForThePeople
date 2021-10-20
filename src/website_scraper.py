from bs4 import BeautifulSoup
import requests


class ReviewScraper:

    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_pages_for_reviews(self, number_of_pages_to_scrape):
        results = []
        for i in range(1, number_of_pages_to_scrape+1):
            all_reviews_on_page = scrape_page_for_paragraph_text_by_class(f'{self.base_url}/page{i}/', "review-content")
            results.extend(all_reviews_on_page)
        return results


# Since this is a static method it was decided to leave this outside the class.
# Could be useful in other scenarios less specific to the ReviewScraper class.
def scrape_page_for_paragraph_text_by_class(url_to_scrape, class_attribute):
    page = requests.get(url_to_scrape)

    parsed_html = BeautifulSoup(page.content, "html.parser")

    content = parsed_html.find_all("p", class_=class_attribute)
    return [c.text.strip() for c in content]

