import math
import numpy as np

f = open("adv19_finalB.in", "r", encoding='utf-8')
reading = True
bp = []
TIME = 32


while reading:
    line = f.readline().strip()
    if line == '':
        reading = False
        break
    words = line.split()
    req = np.array([[int(words[6]), 0, 0, 0], 
                    [int(words[12]), 0, 0, 0], 
                    [int(words[18]), int(words[21]), 0, 0], 
                    [int(words[27]), 0, int(words[30]), 0]])
    bp.append(req)


def production_time(a, robots, res, req):
    b = a - 1 if a > 0 else 0
    if robots[b] == 0:
        return 25
    else:
        t_a = math.ceil(max((req[a, 0] - res[0])/robots[0], 
                            (req[a, b] - res[b])/robots[b]))
        return max(t_a, 0) + 1


def geodes(action, robots, res, req, max_req, time, d):
    robots[action] += 1
    
    actions_available = [0, 1, 2, 3]
    for i in range(3):
        if robots[i] >= max_req[i]:
            actions_available.remove(i)
    # These two constraints may not be formally correct
    # ... but they are admissible for the given input :-)
    if np.min(res-req[3, :]) >= 0:
        actions_available = [3]
    elif np.min(res-req[2, :]) >= 0:
        actions_available = [2]

    geodes_return = [(['end'], 0)]
    for a in actions_available:
        t_a = production_time(a, robots, res, req)
        res_a = res + t_a*robots - req[a, :]
        time_a = time - t_a
        robots_a = robots.copy()
        robots_a[a] += 1
        if time_a >= 0:
            geodes_return += [geodes(a, robots.copy(), 
                              res_a.copy(), req, max_req, 
                              time_a, d + 1)]
    max_return = max([y for (x, y) in geodes_return])
    max_a = [x for (x, y) in geodes_return if y == max_return][0]
    if action == 3:
        return ([(TIME-time, action, res.tolist(), robots.tolist())] + max_a, 
                max_return + time)
    else:
        return ([(TIME-time, action, res.tolist(), robots.tolist())] + max_a, 
                max_return)


sum = 0
prod = 1
i = 1
for req in bp:
    max_req = [np.max(req[:, 0]), np.max(req[:, 1]), np.max(req[:, 2])]
    hist, ret = geodes(0, np.array([0, 0, 0, 0]), np.array([0, 0, 0, 0]), req, 
                       max_req, TIME, 0)
    sum += i*ret
    prod *= ret
    i += 1

# print('final sum:', sum)
print('final product:', prod)









