# Build a CLI program where you give it a research keyword, and it returns a structured list of relevant papers.
import requests
from bs4 import BeautifulSoup

links = {}
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36"
    }

url = "https://arxiv.org/"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    for h in soup.find_all('h2'):
        if h.text == "About arXiv":
            continue
        else:
            for l in h.find_next_sibling('ul').find_all('li'):
                for a in l.find_all('a'):
                    ky = a.text
                    vl = a.get('href')
                    if vl.startswith('/'):
                        vl = url + vl.removeprefix('/')
                    if ky == "new":
                        new_ky = a.find_previous_sibling('a').text + " " + ky.capitalize()
                        links[new_ky] = vl
                        for i in a.find_next_siblings('a', limit=2):
                            new_ky = a.find_previous_sibling('a').text + " " + i.text.capitalize()
                            links[new_ky] = vl
                    elif ky == "recent" or ky == "search":
                        continue
                    else:
                        new_ky = ky
                        links[new_ky] = vl
                    
else:
    print(f"Error {response.status_code}/n{response.text}")