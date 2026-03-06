import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/NIFTY_50"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Find the first wikitable
table = soup.find("table", {"class": "wikitable"})

if table is None:
    print("Table not found on page")
    exit()

companies = []
sectors = []

rows = table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")

    if len(cols) >= 3:
        company = cols[0].text.strip()
        sector = cols[2].text.strip()

        companies.append(company)
        sectors.append(sector)

df = pd.DataFrame({
    "Company": companies,
    "Sector": sectors
})

df.to_csv("data/nifty50.csv", index=False)

print("Data successfully scraped and saved!")
