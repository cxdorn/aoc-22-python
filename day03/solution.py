import io
import sys
import math

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vals = {}
for i in range(52):
    vals[alph[i]] = i+1

f = open("input.in", "r", encoding='utf-8')
reading = True
total = 0
prevr = alph
per = 0

while reading:
    r = f.readline()
    if r == '':
        reading = False
        break
    per += 1
    prevr = ''.join([x for x in r if (prevr.find(x) != -1)])
    # print(prevr)
    if per % 3 == 0:
        total += vals[prevr[0]]
        prevr = alph
    # l = len(r)
    # h = int(l/2)
    # it = [x for x in r[:h] if (r[h:].find(x) != -1)][0]
    # total += vals[it]

print(total)
