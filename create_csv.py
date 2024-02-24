import esv_ranges
import pandas as pd
import numpy as np

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

psdatalist = [i for i in esv_ranges.passage_data if i ]
b = [x[:1] for x in psdatalist]
b = [i for s in b for i in s]
c = [x[1:2] for x in psdatalist]
c = [i for s in c for i in s]
v = [x[2:3] for x in psdatalist]
v = [i for s in v for i in s]
v = [i for s in v for i in s]
v = [i for i in v if i]

book_col = [x for x, i in zip(b,c) for _ in range(i)]
chap_col = [i for s in c for i in range(1,s+1)]
vers_col = v

col_names = ['Book', 'Chapter', 'Number of Verses']

prot_canon = pd.DataFrame([book_col, chap_col, vers_col], index=col_names).T
prot_canon.to_csv('bible.csv', index=False, header=True)