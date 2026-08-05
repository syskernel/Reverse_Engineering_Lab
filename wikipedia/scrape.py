import requests
from bs4 import BeautifulSoup

infobox = {}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
response = requests.get("https://en.wikipedia.org/wiki/World_War_II", headers=headers)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    title = soup.find(id="firstHeading").text.strip()
    last_modified_date = soup.find(id="footer-info-lastmod").text.strip().removeprefix("This page was last edited on ")
    p = soup.find_all('p')
    first_para = p[1].text.strip()
   
else:
    print(f"Error {response.status_code}")