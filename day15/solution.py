import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
ss = []
bs = []
c = set()

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.split()
    x = int(line[2][2:-1])
    y = int(line[3][2:-1])
    t = int(line[-1][2:])
    s = int(line[-2][2:-1])
    ss += [(x, y)]
    bs += [(s, t)]


dist = []

for k in range(len(ss)):
    (s, t) = ss[k]
    (a, b) = bs[k]
    dist += [abs(s-a) + abs(t-b)]

bound = 4000000

for y in range(0, bound):
    if y % 100000 == 0:
        print(y)
    x = 0
    while x < bound:
        uncovered = True
        k = 0
        while uncovered and k < len(ss):
            (s, t) = ss[k]
            m = abs(s-x) + abs(t-y)
            if m <= dist[k]: 
                uncovered = False
                x += dist[k]-m+1
            k += 1
        if uncovered:
            print('SOLUTION: ', (x, y))
            break
