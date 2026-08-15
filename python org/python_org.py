import requests
from bs4 import BeautifulSoup

def org(vers):
    download_files = []
    details = {}
    url = f"https://www.python.org/downloads/release/python-{vers}/"
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    versn = soup.find('header', 'article-header').text.strip().removeprefix('Python ')
    rlz_date = soup.find("strong", string="Release date:").next_sibling.text.strip()
    for i in soup.find_all('div', "featured-download-box"):
        files = {}
        system = i.h3.text.strip()
        url = i.a['href']
        files["System"] = system
        files["URL"] = url
        download_files.append(files)    

    details.update({
        'Verion': versn,
        'Release Date': rlz_date,
        'Download_Files': download_files
        })

    return details