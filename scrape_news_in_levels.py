import requests
import json
from bs4 import BeautifulSoup

URL = 'https://www.newsinlevels.com/page/'
PAGES = 203

data = []
used_links = []
try:
    for j in range(1, PAGES):
        page = requests.get(URL + str(j))
        soup = BeautifulSoup(page.content, 'html.parser')

        links = []
        for art_ref in soup.find_all('div', class_='main-content')[0].find_all('div', class_='fancy-buttons'):
            links.append([a.get('href') for a in art_ref.find_all('a')])

        for l in links:

            d = {}
            for i in range(3):
                if l[i] in used_links:
                    break
                page = requests.get(l[i])
                art_soup = BeautifulSoup(page.content, 'html.parser')
                try:
                    d['level %s' % i] = [p.getText() for p in art_soup.find_all('div', id='nContent')[0].find_all('p')[1:-2]]

                except IndexError:
                    print('skipped 1 article')
                    break
            if d:
                data.append(d)
            used_links.extend(l)
        print(data)
finally:
    with open('data/data_news_in_levels.json', 'w') as f:
        f.write(json.dumps({'news_in_levels': data}))


