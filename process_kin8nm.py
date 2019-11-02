import os
import pandas as pd

fname_list = ['test.vw', 'train.vw', 'validation.vw']

dat = set()

for fname in fname_list:
    path = os.path.join("raw/kin8nm", fname)
    with open(path) as f:
        for line in f.readlines():
            if line in dat:
                raise ValueError("Replicated entry detected!")
            dat.add(line)

#print(len(dat))

assert len(dat) == 8192

mat = []
for d in dat:
    target_s, inp_s = d.strip().split("|n")
    target = float(target_s)
    inp = []
    for s in inp_s.strip().split(' '):
        inp.append(float(s.split(':')[1]))
    mat.append([target] + inp)

df = pd.DataFrame(mat)

endog_columns = ['Y']
exog_columns = ['X{}'.format(i) for i in range(1,9)]

df.columns = endog_columns + exog_columns