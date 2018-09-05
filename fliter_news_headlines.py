from nltk.translate.chrf_score import sentence_chrf
import json

data = {'level1': [], 'level2': []}

normal = []
simple = []
with open('/home/dzvinka/Internship_summer18/datasets/news_articles_simpl/summarization_all.txt') as f:
    i = 0
    while True:
        line = f.readline()

        if not line:
            break
        if i % 2:
            normal.append(line.strip('GO'))
        else:
            simple.append(line.strip('GO'))
        i += 1

print(normal[5])
print(simple[5])
i = 0
for s, n in zip(simple, normal):
    score_chrf = sentence_chrf(s, n)

    if score_chrf > 0.4:
        i += 1
        data['level1'].append(s)
        data['level2'].append(s)
print(i)
    # print(score_chrf)
    # print(s)
    # print(n)
    # print(


with open('data/data_news_headlines_filtered.json', 'w') as f:
    f.write(json.dumps(data))