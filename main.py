from scraper.scraper import BookScraper

def main():
    print("Starting book scraper...")
    scraper = BookScraper()
    scraper.scrape_books(num_pages=3)  # Scrape first 3 pages
    print("Scraping completed!")

if __name__ == "__main__":
    main()