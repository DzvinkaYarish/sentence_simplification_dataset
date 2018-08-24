import requests
import json
from bs4 import BeautifulSoup

URL = 'https://breakingnewsenglish.com/'
MAIN = 'graded-news-stories.html'

data = {'level1': [], 'level2': [], 'level3': []}

try:
    page = requests.get(URL + MAIN)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    art_links = [a.get('href').split('.')[0] for a in soup.find('div', id='primary').find_all('a')]
    print(len(art_links))
    for a_l in art_links[3:]:
        d = []
        for i in range(3):
            page = requests.get(URL + a_l + '-' + str(i) + '.html')
            if page.status_code != 200:
                print('ble')
                d = []
                break

            art_soup = BeautifulSoup(page.content, 'html.parser')

            article = art_soup.findAll('article')[0].getText().split('\n')
            # print(article)
            d.append(''.join([p for p in article if p and not p.startswith('(')]))

        if d:
            for k in range(len(d)):
                data['level%d' % (k + 1)].append(d[k])
        print(len(data['level1']))

finally:
    with open('data/data_breaking_news_english.json', 'w') as f:
        f.write(json.dumps(data))


