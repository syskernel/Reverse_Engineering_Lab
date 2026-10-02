import requests
from bs4 import BeautifulSoup

details = []
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
}

base_url = "https://projecteuler.net/archives"

response = requests.get(base_url, headers=headers)
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