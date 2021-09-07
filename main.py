import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise Exception('response not ok')

text = response.text

soup = BeautifulSoup(text, features="html.parser")

articles = soup.find_all('article')

for article in articles:
    headline = article.h2.a.text
    post_preview_text = article.div.div.text
    post_link = 'https://habr.com' + article.find('h2').find('a').attrs.get('href')
    public_date = article.find('time').attrs.get('title').split(',')[0]

    for search_word in KEYWORDS:
        if (search_word.lower() in headline.lower()) or (search_word.lower() in post_preview_text.lower()):
            print(f'Дата: {public_date} - Заголовок: {headline} - Ссылка: {post_link}')
