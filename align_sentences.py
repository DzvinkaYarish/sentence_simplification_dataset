from __future__ import print_function
import json
import re
from bleualign.align import Aligner

levels = [(1,2), (1,3), (2,3)]

with open('data/data_news_in_levels_new.json') as json_data:
    d = json.load(json_data)

i = 0
for lev in levels:
    aligned_d = {'level%d' % lev[0]: [], 'level%d' % lev[1]: []}
    for art1, art2 in zip(d['level%d' % lev[0]], d['level%d' % lev[1]]):
        try:
            f_art1 = '.\n'.join([s.strip() for s in re.split('[.!;"]', art1)])
            f_art2 = '.\n'.join([s.strip() for s in re.split('[.!;"]', art2)])
            print(f_art1)
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

                print()
                if abs(len(sent[0]) - len(sent[1])) > 2:
                    aligned_d['level%d' % lev[0]].append(sent[0])
                    aligned_d['level%d' % lev[1]].append(sent[1])
                    print(sent[0])
                    print(sent[1])
            # print(len(aligned_d['level1']))
            # break
        except ValueError:
            i += 1
            continue

        finally:
            print(i)
            if len(aligned_d['level%s' % lev[0]]) > 0:
                print('rewrite')
                with open('data/data_news_in_levels_aligned_new_%d_%d.json' % lev, 'w') as f:
                    f.write(json.dumps(aligned_d))