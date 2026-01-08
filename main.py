from scraper.search import find_websites
from scraper.validator import is_real_business
from scraper.extractor import extract_data
import csv
import time
import os

OUTPUT_FILE = "output/leads.csv"

def run():
    print("🔍 Searching for businesses...")
    websites = find_websites()
    print(f"🌐 Found {len(websites)} websites")

    leads = []

    for site in websites:
        print(f"Checking: {site}")
        if is_real_business(site):
            lead = extract_data(site)
            leads.append(lead)
            print(f"✅ Lead found: {lead['company']}")
        time.sleep(2)

    os.makedirs("output", exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["company", "website", "email"])
        writer.writeheader()
        writer.writerows(leads)

    print(f"\n📁 Saved {len(leads)} qualified leads to {OUTPUT_FILE}")

if __name__ == "__main__":
    run()
