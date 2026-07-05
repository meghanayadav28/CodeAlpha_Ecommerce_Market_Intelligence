import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# A highly stable, static URL on the test site
BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

scraped_products = []

print("🚀 Starting the backup web scraping pipeline...")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(BASE_URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Target the main product containers
    product_cards = soup.find_all("div", class_="card-body")
    
    for card in product_cards:
        try:
            # 1. Title
            title_el = card.find("a", class_="title")
            if not title_el:
                continue
            title = title_el.text.strip()
            
            # 2. Price
            price = card.find("h4", class_="price").text.strip()
            
            # 3. Description
            description = card.find("p", class_="description").text.strip()
            
            scraped_products.append({
                "Product_Name": title,
                "Price_Raw": price,
                "Specifications": description
            })
        except Exception:
            continue

print(f"✨ Process Complete! Total items collected: {len(scraped_products)}")

# Convert and save
df = pd.DataFrame(scraped_products)
df.to_csv("raw_market_intelligence.csv", index=False)
print("💾 Saved to 'raw_market_intelligence.csv'!")

print("\n🔍 Sneak peek of your collected data:")
print(df.head(3))