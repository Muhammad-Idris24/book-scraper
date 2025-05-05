import pandas as pd
from scraper.utils import make_request, parse_html, clean_text
from scraper.config import BASE_URL, OUTPUT_FILE

class BookScraper:
    def __init__(self):
        self.data = []
        
    def scrape(self, num_pages=1):  # Changed from scrape_books to scrape
        """Scrape books from the website"""
        for page in range(1, num_pages + 1):
            url = f"{BASE_URL}catalogue/page-{page}.html"
            print(f"Scraping page {page}...")
            
            try:
                response = make_request(url)
                soup = parse_html(response.text)
                self._extract_books(soup)
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                
        self._save_to_csv()
        
    def _extract_books(self, soup):
        """Extract book details from the page"""
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = clean_text(book.h3.a['title'])
            price = clean_text(book.find('p', class_='price_color').text)
            availability = clean_text(book.find('p', class_='instock').text)
            rating = book.p['class'][1]  # e.g., 'Three' for 3-star rating
            
            self.data.append({
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            })
    
    def _save_to_csv(self):
        """Save scraped data to CSV file"""
        df = pd.DataFrame(self.data)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Data saved to {OUTPUT_FILE} with {len(df)} records")