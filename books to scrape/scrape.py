import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'xml')
    for article in soup.find_all('article'):
        link = article.find('a')
        title = article.find('h3').text
        p_tag = article.find_all('p')
        price = p_tag[1].text
        avlbl = p_tag[2].text
        rating = p_tag[0]['class'].removeprefix('star-rating')
        
else:
    print(f"Error {response.status_code}: {response.text}")