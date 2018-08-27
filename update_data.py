import requests
import json
import time
import sys
from bs4 import BeautifulSoup
from scrape_news_in_levels import get_text

URL = 'https://www.newsinlevels.com'

with open('data/data_news_in_levels_new.json') as json_data:
    data = json.load(json_data)


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


LAST_DATE = time.strftime('%Y-%m-%d', time.localtime(int(sys.argv[1])))



for news, refs in zip(soup.find_all('div', class_='news-excerpt'), soup.find_all('div', class_='fancy-buttons')):
    date = news.getText().split()[0]
    try:
        date = '{2}-{1}-{0}'.format(date.split('-')[0], date.split('-')[1], date.split('-')[2])
        print(LAST_DATE)
        print(date)
    except IndexError:
        continue
    if date <= LAST_DATE:
        break
    links = [a.get('href') for a in refs.find_all('a')]
    d = []
    for i in range(3):
        d.append(get_text(links[i]))
    if all(d):
        for k in range(len(d)):
            data['level%d' % (k + 1)].append(d[k])
    i += 1




with open('data/data_news_in_levels_new.json', 'w') as f:
            f.write(json.dumps(data))

