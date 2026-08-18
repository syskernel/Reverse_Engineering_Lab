import requests
from bs4 import BeautifulSoup

def infobox(): 
    info = {}
    table = soup.find('table', "infobox vevent")
    for sup in table.find_all("sup"):
        sup.decompose()
    for tr in table.find_all('tr'):
        if tr.th != None:
            value = tr.th.next_sibling
            if value == None:
                ky = tr.th.text.strip()
                nxt = tr.next_sibling
                if nxt.td != None:
                    vl = nxt.get_text(" ", strip=True)
                    if not vl or not ky:
                        continue
                    else:
                        info[ky] = vl
                        
            elif value.name == 'td':
                ky = tr.th.text.strip()
                vl = value.get_text(" ", strip=True)
                if not vl or not ky:
                    continue
                else:
                    info[ky] = vl

    return info

referense = []
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)", headers=headers)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    title = soup.find(id="firstHeading").text.strip()
    last_modified_date = soup.find(id="footer-info-lastmod").text.strip().removeprefix("This page was last edited on ")
    p = soup.find_all('p')
    first_para = p[1].text.strip()

    # infobox
    print(len(infobox()))

    # Table of Contents()
    #contents = soup.find('ul', "vector-toc-contents")
    #for ls in contents.find_all('li', "vector-toc-list-item vector-toc-level-1"):
    #    word = ls.get_text(" ", strip=True)
    # Images
    # Referencescite class=
    #for i in soup.find_all("cite", "citation web cs1"):
    #    referense.append(i.get_text(" ", strip=True))
    # External Links
    # Categories
    # Internal Links
    # Statistics
   
else:
    print(f"Error {response.status_code}")
