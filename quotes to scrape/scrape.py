import requests
import json

quotes = []
n = 1
url = "https://quotes.toscrape.com/js/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}

while n<11:
    r = requests.get(url, headers=headers)  

    if r.status_code == 200:
        html = r.text
        data = html.rfind("var data")
        start = html.find("[", data)
        end = html.find("];", data) + 1
        json_string = html[start:end]
        qts = json.loads(json_string)

        for quote in qts:
            qt = quote['text']
            author = quote["author"]["name"]
            quotes.append({
                "Author": author,
                "Quote": qt
            })  

        print(f"Got page {n}")
        n += 1
        url = f"https://quotes.toscrape.com/js/page/{n}/"

print(quotes)