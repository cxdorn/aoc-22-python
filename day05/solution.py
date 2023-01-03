import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
setup = {}
settingup = True
moving = False
stacks = 9
for i in range(stacks):
    setup[i] = []

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    if moving:
        line = line.split()
        repet = int(line[1])
        source = int(line[3])-1
        target = int(line[5])-1
        # print(setup, target, source, repet)
        setup[target] += setup[source][-repet:]
        for _ in range(repet):
            setup[source].pop()
    if line == '\n':
        settingup = False
        moving = True
        # print(setup)
    if settingup:
        for i in range(stacks):
            letter = line[1 + i*4]
            if letter != ' ':
                setup[i].insert(0, letter)

finalstr = ''
for i in range(stacks):
    finalstr += setup[i][-1]
print(finalstr)
