import io
import sys
import math


f = open("input.in", "r", encoding='utf-8')
reading = True
pairs = []
mod = 0
pair = [[[2]], [[6]]]
pairs += [pair.copy()]

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    if line == '\n':
        mod = 0
    elif mod == 0:
        pair[0] = eval(line[:-1])
        mod += 1
    elif mod == 1:
        pair[1] = eval(line[:-1])
        pairs += [pair.copy()]


def cpr(a, b):
    c = 'cont'

    (al, bl) = (type(a) is list, type(b) is list)
    if al and not bl:
        b = [b]
    if bl and not al:
        a = [a]

    if not al and not bl:
        if a < b:
            c = 'right'
        elif a == b:
            c = 'cont'
        elif a > b:
            c = 'wrong'
    else:
        (ae, be) = (a == [], b == [])
        if ae and not be:
            c = 'right'
        elif be and not ae:
            c = 'wrong'
        elif be and ae:
            c = 'cont'
        else:
            c = cpr(a[0], b[0])
            if c == 'cont':
                c = cpr(a[1:], b[1:])

    return c


def ordered_insert(t, a):
    m = len(t)
    if m == 0:
        return [a]
    if m == 1:
        if cpr(t[0], a) == 'right':
            return t.copy() + [a]
        else:
            return [a] + t.copy()
    h = round(m/2)
    t1 = t[:h]
    t2 = t[h:]
    if cpr(t[h], a) == 'right':
        t2 = ordered_insert(t2, a)
    else:
        t1 = ordered_insert(t1, a)
    t12 = t1.copy() + t2.copy()
    return t12


tbl = []
for [a, b] in pairs:
    tbl = ordered_insert(tbl, a)
    tbl = ordered_insert(tbl, b)


i, j, k = 1, 0, 0
for x in tbl:
    if x == [[2]]:
        j = i
    if x == [[6]]:
        k = i
    i += 1

print(j*k)
