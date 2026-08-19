import requests
from bs4 import BeautifulSoup

def internal_links(soup):
    links = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if href.startswith("https://en.wikipedia.org/wiki/"):
            links.append(a.get('href'))

    return links

def external_links(soup):
    links = {}
    external = soup.find('ul', id="mwEkc" )
    for ls in external.find_all('li'):
        ky = ls.get_text(" ", strip=True)
        vl = ls.a.get('href')
        links[ky] = vl

    return links

def refer(soup):
    rfrnc = []
    reference = soup.find('div', "mw-references-wrap mw-references-columns")
    for ls in reference.find_all('li'):
        sp = ls.find_all('span')[2].text.strip()
        rfrnc.append(sp)

    return rfrnc

def infobox(soup): 
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

def content(soup):
    content = []
    contents = soup.find('ul', "vector-toc-contents")
    for ls in contents.find_all('li', "vector-toc-list-item vector-toc-level-1"):
        if ls.div.span != None:
            cntnt = ls.div.find_all('span')[1].text.strip()
            if ls.ul.li != None:
                ct = []
                sub_content = {}
                for l in ls.ul.find_all('li'):
                    cntnt_l = l.div.find_all('span')[1].text.strip()
                    ct.append(cntnt_l)
                sub_content[cntnt] = ct
                content.append(sub_content)
            else:
                content.append(cntnt)

    return content

def main():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
    }
    response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)", headers=headers)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        title = soup.find(id="firstHeading").text.strip()
        last_modified_date = soup.find(id="footer-info-lastmod").text.strip().removeprefix("This page was last edited on ") 
        first_para = soup.find_all('p')[1].text.strip()

        # Images
        # Categories

        # Statistics
    
    else:
        print(f"Error {response.status_code}")

main()