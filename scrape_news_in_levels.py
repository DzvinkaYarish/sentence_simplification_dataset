import requests
import json
from bs4 import BeautifulSoup

URL = 'https://www.newsinlevels.com/page/'
PAGES = 203

data = {'level1': [], 'level2': [], 'level3': []}
used_links = []


def get_text(link):
    pg = requests.get(link)
    art_soup = BeautifulSoup(pg.content, 'html.parser')
    try:
        return ''.join([p.getText() for p in art_soup.find_all('div', id='nContent')[0].find_all('p')[1:-2]])
    except IndexError:
        return None


if __name__ == '__main__':
    try:
        for j in range(1, PAGES):
            page = requests.get(URL + str(j))
            soup = BeautifulSoup(page.content, 'html.parser')

            links = []
            for art_ref in soup.find_all('div', class_='main-content')[0].find_all('div', class_='fancy-buttons'):
                links.append([a.get('href') for a in art_ref.find_all('a')])

            for l in links:

                d = []
                for i in range(3):
                    if l[i] in used_links:
                        break
                    d.append(get_text(l[i]))

                if all(d):
                    for k in range(len(d)):
                        data['level%d' % (k + 1)].append(d[k])
                used_links.extend(l)
                print(len(data['level1']))
    finally:
        with open('data/data_news_in_levels.json', 'w') as f:
            f.write(json.dumps(data))


