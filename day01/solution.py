import io
import sys
import math

elf_no = 1
max = [0, 0, 0]
f = open("input.in", "r", encoding='utf-8')
reading = True
total = 0

while reading:
    cal = f.readline()
    if cal == '':
        reading = False
    if cal == '\n' or cal == '':
        if max[2] < total:
            if max[1] < total:
                if max[0] < total:
                    max[2] = max[1]
                    max[1] = max[0]
                    max[0] = total
                else:
                    max[2] = max[1]
                    max[1] = total
            else:
                max[2] = total
        total = 0
    else:
        total += int(cal)

print(sum(max))
