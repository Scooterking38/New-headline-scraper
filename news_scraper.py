import requests
from bs4 import BeautifulSoup
import os

# URL of the Times of India homepage
url = "https://timesofindia.indiatimes.com/"

# Fetch the page
response = requests.get(url, timeout=30)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all headline divs
headline_divs = soup.find_all("div", class_="CRKrj")

headlines = [div.get_text(strip=True) for div in headline_divs if div.get_text(strip=True)]

# Save headlines to a file
file_path = os.path.join(os.getcwd(), "headlines.txt")
with open(file_path, "w", encoding="utf-8") as f:
    for headline in headlines:
        f.write(headline + "\n")

print(f"✅ {len(headlines)} headlines saved to: {file_path}")
