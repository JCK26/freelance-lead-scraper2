import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BusinessLeadBot/1.0)"
}

def extract_data(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(" ")

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = emails[0] if emails else None

    company = soup.title.string.strip() if soup.title else "Unknown"

    return {
        "company": company,
        "website": url,
        "email": email
    }
