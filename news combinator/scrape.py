import requests
from bs4 import BeautifulSoup
import pandas as pd

links = []
titles = []
authors = []
scores = []
comments = []

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
        links.append(link)
        titles.append(title)
        authors.append(author)

    for i in soup.find_all('td', 'subtext'):
        score_l = i.find('span', 'score')
        if score_l is None:
            scores.append('N/A')
        else:
            score = score_l.text.strip().removesuffix(' points')
            scores.append(score)

        comment_l = i.find('span', 'subline')
        if comment_l is None:
            comments.append('N/A')
        else:
            a = comment_l.find_all('a')
            comment = a[3].text.strip()
            comments.append(comment)

else:
    print(f"Error {response.status_code}")

df = pd.DataFrame({
    "TITLE": titles,
    "LINK": links,
    "AUTHOR": authors,
    "SCORE": scores,
    "COMMENTS": comments
})

df.to_excel("news.xlsx", index=False)
print("Excel file saved!")