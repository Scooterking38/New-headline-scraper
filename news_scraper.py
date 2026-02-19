import requests
from bs4 import BeautifulSoup
import os

response = requests.get("https://timesofindia.indiatimes.com/", timeout=30)
response.raise_for_status()

headline_divs = BeautifulSoup(response.text, "html.parser").find_all("div", class_="CRKrj")

headlines = [div.get_text(strip=True) for div in headline_divs if div.get_text(strip=True)]

file_path = os.path.join(os.getcwd(), "headlines.txt")
with open(file_path, "w", encoding="utf-8") as f:
    for headline in headlines:
        f.write(headline + "\n")

print(f'✅ {len(headlines)} headlines saved to: {file_path}')

