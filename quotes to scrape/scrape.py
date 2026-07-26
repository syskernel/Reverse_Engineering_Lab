import requests
import json

url = "https://quotes.toscrape.com/js/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'}
r = requests.get(url, headers=headers)

if r.status_code == 200:
    html = r.text
    data = html.rfind("var data")
    start = html.find("[", data)
    end = html.find("];", data) + 1
    json_string = html[start:end]
    quotes = json.loads(json_string)
    for quote in quotes:
        text = quote["text"].removeprefix('"')
        author = quote["author"]["name"]
        print(f"{text}\n by {author}")