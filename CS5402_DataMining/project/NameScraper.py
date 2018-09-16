"""
NameScraper.py is a program written to scrape random summoner names from the na.op.gg website.
The official Riot API does not expose an endpoint to get a random list of names.

Result: A .txt file containing a random list of 10000 summoner names and associated ladder ranking.
"""

import bleach, requests
from bs4 import BeautifulSoup

# Setup -- There are 15860 pages of ranked players on op.gg right now
base_url = "http://na.op.gg/ranking/ladder/page="
r = requests.get(base_url + "=1001")
soup = BeautifulSoup(r.content, 'html.parser')

print(soup)

# Parse
# soup = soup.find_all("tr", {"class":"ranking-table__row"})
# for row in soup:
#     summonerCell = row.find("td", {"class":"ranking-table__cell--summoner"})
#     summonerName = summonerCell.find("span")
#     print(summonerName.text)

# print(soup)