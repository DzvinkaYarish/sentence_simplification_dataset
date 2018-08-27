# run with python 2.7

from __future__ import print_function
import json
import re
from bleualign.align import Aligner

aligned_d = {'level2': [], 'level3': []}

with open('../../sentecnce_simplification_dataset/data/data_news_in_levels.json') as json_data:
    d = json.load(json_data)

i = 0
for art1, art2 in zip(d['level2'], d['level3']):
    try:
        f_art1 = '.\n'.join([s.strip() for s in re.split('[.!;]', art1)])
        f_art2 = '.\n'.join([s.strip() for s in re.split('[.!;]', art2)])

        options = {
                    # source and target files needed by Aligner
                    # they can be filenames, arrays of strings or io objects.
                    'srcfile': f_art1,
                    'targetfile': f_art2,
                    # translations of srcfile and targetfile, not influenced by 'factored'
                    # they can be filenams, arrays of strings or io objects, too.
                    'srctotarget': [f_art1],
                    'targettosrc': [],
                    # passing filenames or io object for them in respectly.
                    # if not passing anything or assigning None, they will use StringIO to save results.
                    'output-src': None, 'output-target': None,
                    # other options ...
                    }
        a = Aligner(options)
        a.mainloop()
        res = a.results
        for sent in res:
            print(sent[0])
            print(sent[1])
            print()
            aligned_d['level2'].append(sent[0])
            aligned_d['level3'].append(sent[1])
        print(len(aligned_d['level2']))
        # break
    except ValueError:
        i += 1
        continue

    finally:
        print(i)
        with open('../../sentecnce_simplification_dataset/data/data_news_in_levels_aligned_2_3.json', 'w') as f:
            f.write(json.dumps(aligned_d))