import io
import sys
import math
import numpy as np

f = open("input.in", "r", encoding='utf-8')
reading = True

struct = {}
index = []
rindex = []
index_dict = {}
impt = []
flws = {}
id = 0

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.split()
    name = line[1]
    struct[name] = {}
    flow = int(line[4][5:-1])
    struct[name]['flow'] = flow
    tuns = []
    for i in range(9, len(line)):
        tuns += [line[i] if line[i][-1] != ',' else line[i][:-1]] 
    struct[name]['tun'] = tuns
    index += [name]
    index_dict[name] = id
    if flow > 0:
        impt += [id]
    flws[id] = flow
    id += 1

n = len(index)
dist = np.ones((n, n))*(n+1)

reach = {}
for i in range(n):
    reach[i] = {i}
    dist[i, i] = 0

for i in range(n):
    for t in struct[index[i]]['tun']:
        j = index_dict[t]
        dist[i, j] = 1
        dist[j, i] = 1
        reach[i].add(j)
        reach[j].add(i)

for k in range(2, n):
    for i in set(range(n)):
        for j in set(range(n)) - reach[i]:
            for l in reach[i] & reach[j]:
                if dist[i, l] + dist[l, j] == k:
                    dist[i, j] = k
                    dist[j, i] = k
                    reach[i].add(j)
                    reach[j].add(i)

start = index_dict['AA']
time = 30
time2 = 26

def recurs2(currme, currel, minme, minel, o):
    vals = []
    for i in set(impt) - set(o):
        if len(o) == 3:
            print('testing ', i, ' from ', o)
        dme = dist[currme, i]
        dele = dist[currel, i]
        remme = minme-dme-1
        remel = minel-dele-1
        oi = o + [i]
        if remme >= 0 and dme < 12:
            rec = recurs2(i, currel, remme, minel, oi.copy())
            vals += [rec]
        if remel >= 0 and dele < 12:
            rec = recurs2(currme, i, minme, remel, oi.copy())
            vals += [rec]

    max_prod = 0 if vals == [] else max(vals)
    
    if currme == o[-1]:
        return flws[o[-1]]*minme + max_prod
    else:
        return flws[o[-1]]*minel + max_prod


def recurs3(curr, mins, o, ind):
    vals = []
    testing = impt1 if ind == 1 else impt2
    for i in set(testing) - set(o):
        d = dist[curr, i]
        rem = mins-d-1
        oi = o + [i]
        if rem >= 0:
            rec = recurs3(i, rem, oi.copy(), ind)
            vals += [rec]

    max_prod = 0 if vals == [] else max(vals) 
    return flws[curr]*mins + max_prod


def recurs(curr, mins, o):
    vals = []

    for i in set(impt) - set(o):
        d = dist[curr, i]
        rem = mins-d-1
        oi = o + [i]
        if rem >= 0:
            rec = recurs(i, rem, oi.copy())
            vals += [rec]

    max_prod = 0 if vals == [] else max(vals) 
    return flws[curr]*mins + max_prod

result = recurs(start, time, [])
print(result)
print(len(impt))

impt1, impt2 = [], []
t = len(impt)
eltot = []

for i in range(1 << t):
    impt1, impt2 = [], []
    for k in range(t):
        if (i >> k) & 1:
            impt1 += [impt[k]]
        else:
            impt2 += [impt[k]]

    if i % 10 == 0:
        print('Trying with code ', i)
    eltot += [recurs3(start,time2,[],1) + recurs3(start,time2,[],2)]

print(max(eltot))
