from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

# Setup Chrome options
options = Options()
options.add_argument("--headless")  # Run without opening window
service = Service(executable_path="chromedriver.exe")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://timesofindia.indiatimes.com/")
time.sleep(5)  # Wait for page to load

# Parse the page
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Find headlines
headlines = soup.select("h2, h3, .headline, .title")

# Set path to save file on Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
file_path = os.path.join(desktop_path, "headlines.txt")

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