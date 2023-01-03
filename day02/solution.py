import io
import sys
import math

ind = {'roc': 0, 'pap': 1, 'sci': 2}
rev = ['roc', 'pap', 'sci']
val_shap = {'roc': 1, 'pap': 2, 'sci': 3}
val_out = [3, 0, 6]
co = {'A': 'roc', 'B': 'pap', 'C': 'sci'}
ct = {'X': 2, 'Y': 0, 'Z': 1}

f = open("input.in", "r", encoding='utf-8')
reading = True
total = 0

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    op, act = line.split()
    op = co[op]
    me = rev[(ind[op] + ct[act]) % 3]
    i = ind[op] - ind[me] % 3
    total += val_out[i] + val_shap[me]

print(total)
