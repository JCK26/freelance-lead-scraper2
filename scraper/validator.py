import requests
from bs4 import BeautifulSoup
import tldextract
import whois
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BusinessLeadBot/1.0)"
}

BUSINESS_KEYWORDS = [
    "virtual assistant",
    "administrative support",
    "back office",
    "operations",
    "admin assistant",
    "outsourcing"
]

def is_real_business(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ").lower()

        if not any(k in text for k in BUSINESS_KEYWORDS):
            return False

        if not soup.find("a", href=re.compile("contact|about", re.I)):
            return False

        domain = tldextract.extract(url).registered_domain
        w = whois.whois(domain)

        if not w.creation_date:
            return False

        return True

    except:
        return False
