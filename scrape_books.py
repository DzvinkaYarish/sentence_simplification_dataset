import requests
import json
from bs4 import BeautifulSoup

URL = 'http://thelittleprinceinlevels.com/level'
data = {'level1': [], 'level3': []}

for l in range(1, 4, 2):

    for ch in range(28):
        try:
            page = requests.get(URL + str(l + 1) + '/chapter' + str(ch + 1) + '/')
            soup = BeautifulSoup(page.content, 'html.parser')
            text = [p.getText() for p in soup.find('div', class_='et_pb_text et_pb_bg_layout_light et_pb_text_align_left').find_all('p')]
            if text[0].startswith('LEV'):
                data['level%s' % l].append(' '.join(text[2:]))
            else:
                data['level%s' % l].append(' '.join(text[1:]))
            print(len(data['level1']))
        finally:
            with open('data/data_little_prince.json', 'w') as f:
                f.write(json.dumps(data))
