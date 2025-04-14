import time
from random import uniform
from bs4 import BeautifulSoup
import requests
from scraper.config import DELAY, HEADERS

def make_request(url):
    """Make HTTP request with proper headers and delay"""
    time.sleep(uniform(DELAY*0.5, DELAY*1.5))  # Randomize delay
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Raise exception for bad status codes
    return response

def parse_html(html_content):
    """Parse HTML content with BeautifulSoup"""
    return BeautifulSoup(html_content, 'html.parser')

def clean_text(text):
    """Clean and normalize text"""
    if text:
        return ' '.join(text.strip().split())
    return None