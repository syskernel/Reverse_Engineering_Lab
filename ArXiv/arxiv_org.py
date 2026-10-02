import requests
from bs4 import BeautifulSoup
import sys

def get_link():
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
                                vl = i.get('href')
                                if vl.startswith('/'):
                                    vl = url + vl.removeprefix('/')
                                links[new_ky] = vl
                        elif ky == "recent" or ky == "search":
                            continue
                        else:
                            new_ky = ky
                            links[new_ky] = vl

    return links

def main():
    lnk = get_link()
    if len(sys.argv) == 1:
        result = "No Keyword Searched"
    elif len(sys.argv) > 2:
        result = "Search for one keyword at a time"
    elif not lnk:
        result = "No Links found"
    elif sys.argv[1] not in lnk.keys():
        result = "Keyword not found"
    else:
        result = lnk[sys.argv[1]]
    print(result)

if __name__ == '__main__':
    main()