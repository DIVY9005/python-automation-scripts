import requests
from bs4 import BeautifulSoup

# Step 1: Make request
url = "https://www.inshorts.com/en/read"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Extract headlines
headlines = soup.find_all("span", class_="news-card-title")

print("Top News Headlines:\n")
for i, headline in enumerate(headlines[:10]):
    print(f"{i+1}. {headline.text.strip()}")
