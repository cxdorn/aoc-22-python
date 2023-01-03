import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
rock = set()
sand = set()

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.split()
    s, t = -1, -1
    for w in line:
        if w != '->':
            a, b = [int(c) for c in w.split(',')]
            if s != -1 and t != -1:
                while s != a:
                    rock.add((s, b))
                    s += int((a - s)/abs(a - s))
                while t != b:
                    rock.add((a, t))
                    t += int((b - t)/abs(b - t))
            else: 
                s, t = a, b
            rock.add((s, t))


falltime = 0
s = (500, 0)
floor = max([x for (y, x) in rock]) + 2

while (500, 0) not in sand:
    # Possible positions for falling
    pos = [(s[0], s[1]+1),
           (s[0]-1, s[1]+1),
           (s[0]+1, s[1]+1)]

    while pos != []:
        if pos[0] not in sand and pos[0] not in rock and pos[0][1] != floor:
            s = pos[0]
            falltime += 1
            break
        del pos[0]

    if pos == []:
        sand.add(s)
        s = (500, 0)
        falltime = 0

print(floor)
print(len(sand))
