from decouple import config

BASE_URL = "http://books.toscrape.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
DELAY = 2  # seconds between requests
OUTPUT_FILE = "data/scraped_data.csv"