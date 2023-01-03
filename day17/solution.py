import io
import sys
import math
import numpy as np


sim_size = 1000000
rock_no = 1000000000000
stuff = np.zeros((7, sim_size))

shapes = {}

shapes[0] = np.array([[1],
                      [1],
                      [1],
                      [1]])
shapes[1] = np.array([[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]])
shapes[2] = np.array([[1, 0, 0],
                      [1, 0, 0],
                      [1, 1, 1]])
shapes[3] = np.array([[1, 1, 1, 1]])
shapes[4] = np.array([[1, 1],
                      [1, 1]])

maxh = 0
period_maxh = 0

f = open("input.in", "r", encoding='utf-8')
winds = f.readline()[:-1]
w_dict = {'>': +1, '<': -1}
wi = 0
wilen = len(winds)


def is_solid(a):
    solid = True
    for x in a:
        if sum(x) == 0:
            solid = False
    return solid


def has_space(r, x, y, i):
    w, h = r.shape
    if 0 <= x and x + w <= 7 and 0 <= y and np.max(stuff[x:x+w, y:y+h]+r) < 2:
        return True
    else:
        return False


patterns = {}
period_found = False
i = 0

actual_maxh = 0
while i < rock_no:
    r = shapes[i % 5]
    w, h = r.shape
    stationary = False
    (x, y) = (2, maxh + 4)
    while not stationary:
        if has_space(r, x, y-1, i):
            y -= 1
        else:
            stationary = True
            stuff[x:x+w, y:y+h] += r
            maxh = max(maxh, y+h)
            # Check for patterns
            top4 = stuff[0:7, maxh-4:maxh].tolist()
            if is_solid(top4) and not period_found:
                pat = (i % 5, wi % wilen, top4)
                if pat in patterns.values():
                    prev_i, prev_h = list(patterns.keys())[list(patterns.values()).index(pat)]
                    period_i, period_h = i - prev_i, maxh - prev_h
                    rem_periods = math.floor((rock_no - i) / period_i)
                    i = i + rem_periods * period_i
                    period_maxh = rem_periods * period_h
                    period_found = True
                else:
                    patterns[(i, maxh)] = pat
            break
        
        wd = w_dict[winds[wi % wilen]]
        if has_space(r, x + wd, y, i):
            x += wd
        wi += 1

    i += 1

print(maxh + period_maxh)

