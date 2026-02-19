import requests
from bs4 import BeautifulSoup
import os

url = "https://timesofindia.indiatimes.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.7632.109 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=30)
if response.status_code != 200:
    raise Exception(f"Failed to fetch page: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.select("h2, h3, .headline, .title")

# Set path to save file on Desktop
file_path = os.path.join(os.getcwd(), "headlines.txt")

# Write headlines
if headlines:
    with open(file_path, "w", encoding="utf-8") as file:
        count = 0
        for h in headlines:
            text = h.get_text(strip=True)
            if text:
                file.write(text + "\n")
                count += 1
            if count == 10:  # Only top 10 headlines
                break
    print(f"✅ Headlines saved to: {file_path}")
else:

    print("❌ No valid headlines found.")




