import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
total = 0


def overlap(a_0, a_1, b_0, b_1):
    if a_1 < b_0:
        return False
    elif b_1 < a_0:
        return False
    else:
        return True


while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    l, r = line.split(',')
    li = [int(x) for x in l.split('-')]
    ri = [int(x) for x in r.split('-')]
    print(li)
    print(ri)
    if overlap(li[0], li[1], ri[0], ri[1]):
        total += 1

print(total)
