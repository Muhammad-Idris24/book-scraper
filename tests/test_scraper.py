import unittest
from unittest.mock import patch, MagicMock
from scraper.scraper import BookScraper
from bs4 import BeautifulSoup

class TestBookScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = BookScraper()
        
    @patch('scraper.utils.make_request')
    def test_scrape_books(self, mock_request):
        # Mock response
        mock_response = MagicMock()
        mock_response.text = """
        <html>
            <body>
                <article class="product_pod">
                    <h3><a title="Book Title">Book Title</a></h3>
                    <p class="price_color">£10.00</p>
                    <p class="instock">In stock</p>
                    <p class="star-rating Three"></p>
                </article>
            </body>
        </html>
        """
        mock_request.return_value = mock_response
        
        # Test scraping
        self.scraper.scrape_books(num_pages=1)
        
        # Verify results
        self.assertEqual(len(self.scraper.data), 20)  # Assuming 20 books per page
        self.assertEqual(self.scraper.data[0]['title'], "Book Title")
        self.assertEqual(self.scraper.data[0]['price'], "£10.00")
        self.assertEqual(self.scraper.data[0]['availability'], "In stock")
        self.assertEqual(self.scraper.data[0]['rating'], "Three")

    def test_clean_text(self):
        from scraper.utils import clean_text
        self.assertEqual(clean_text("  hello  world  "), "hello world")
        self.assertEqual(clean_text(None), None)
        self.assertEqual(clean_text(""), None)

if __name__ == '__main__':
    unittest.main()