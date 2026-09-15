import requests
from bs4 import BeautifulSoup
import pandas as pd

info = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

url = "https://sih.gov.in/sih2026PS"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    for tr in soup.tbody.find_all('tr'):
        if tr.parent.name != 'tbody':
                continue
        organisation = tr.find_all('td')[1].text.strip()
        title = tr.find_all('td')[2].a.text.strip()
        category = tr.find_all('td')[13].text.strip()
        number = tr.find_all('td')[14].text.strip()
        count = tr.find_all('td')[15].text.strip()
        theme = tr.find_all('td')[16].text.strip()
        sub_date = tr.find_all('td')[17].text.strip()
        info.append({
            "Organisation": organisation,
            "Problem Statement Title": title,
            "Category": category,
            "PS Number": number,
            "Ideas Count": count,
            "Theme": theme,
            "Deadline": sub_date
        })
            
else:
    print(f"Error {response.status_code}")

df = pd.DataFrame(info)
df.to_excel("Problems.xlsx", index=False)