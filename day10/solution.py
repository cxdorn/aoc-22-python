import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
Xval = []
cache = 1

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.split()
    if line[0] == 'noop':
        Xval += [cache]
    if line[0] == 'addx':
        Xval += [cache, cache]
        cache = cache + int(line[1])


print_str = ''

for i in range(240):
    if i % 40 == 0 and i > 0:
        print_str += '\n'
    h = i % 40
    if Xval[i] - 1 <= h and Xval[i] + 1 >= h:
        print_str += '#'
    else:
        print_str += '.'

print(len(Xval))
print(print_str)
