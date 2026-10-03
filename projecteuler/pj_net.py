import requests
from bs4 import BeautifulSoup
import pandas as pd

details = []
n = 0
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}

base_url = "https://projecteuler.net/archives"

while n<22:
    n += 1
    if n==1:
        url = base_url
    elif 1<n<22:
        url = base_url + f";page={n}"
    else:
        url = "https://projecteuler.net/recent"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        soup.find(id="problems_table")
        for tr in soup.find_all('tr'):
            if tr.contents[0].name == 'th':
                continue
            cell = tr.find_all('td')
            num = cell[0].text
            title = cell[1].text
            url = "https://projecteuler.net/" + cell[1].a.get('href')
            solved = cell[2].text   

            details.append({
                "Problem": num,
                "Title": title,
                "Problem URL": url,
                "Solved By": solved
            })  

    else:
        print(f"Error {response.status_code} : {response.text}")

df = pd.DataFrame(details)
df.to_excel("problems.xlsx", index=False)
print("Saved excel file!")