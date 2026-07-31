import requests
from bs4 import BeautifulSoup

n = 0
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}
url = "https://news.ycombinator.com/"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    for i in soup.find_all('span', 'titleline'):
        link = i('a')[0].get('href')
        title = i.text.strip()
        author = url + i('a')[1].get('href')
    for i in soup.find_all('span', 'score'):
        score = i.text.strip().removesuffix(' points')
    for span in soup.find_all('span', 'subline'):
        a = span.find_all('a')
        comments = a[3].text.strip()

else:
    print(f"Error {response.status_code}")