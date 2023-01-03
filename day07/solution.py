import io
import sys
import math


f = open("input.in", "r", encoding='utf-8')
reading = True

data = []
currentdir = ['']

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                a = 1
                currentdir.pop()
            else:
                data += [{'path': currentdir.copy(), 'name': line[2], 'type':
                          'fol', 'size': -1}]
                currentdir += [line[2]]
    elif line[0] != 'dir':
        data += [{'path': currentdir.copy(), 'name': line[1], 'type': 'fil',
                  'size': int(line[0])}]


folders = [x for x in data if x['type'] == 'fol']
files = [x for x in data if x['type'] == 'fil']
folder_size = {}


def recur_size(path):
    total_size = 0
    files_size = sum([x['size'] for x in files if x['path'] == path])
    total_size += files_size
    for x in [y['name'] for y in folders if y['path'] == path]:
        rpath = path + [x]
        total_size += recur_size(rpath)
    folder_size[' '.join(path)] = total_size
    return total_size


recur_size([''])
for x in folders:
    x['size'] = folder_size[' '.join(x['path'] + [x['name']])]

need = 30000000 - (70000000 - folders[0]['size'])
available = []

for x in folders:
    if need <= x['size']:
        available += [x['size']]

print(min(available))
