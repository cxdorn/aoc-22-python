import io
import sys
import math

f = open("input.in", "r", encoding='utf-8')
reading = True
m = {}
curr_monk = -1

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    if line != '\n':
        line_split = line.split()
        # print(line_split)
        if line_split[0] == "Monkey":
            curr_monk += 1
            m[curr_monk] = {}
        if line_split[0] == "Starting":
            item_nums = [int(x) for x in line.split(':')[1].split(',')]
            m[curr_monk]['itm'] = item_nums
        if line_split[0] == "Operation:":
            m[curr_monk]['op'] = eval('lambda old: ' + line.split('=')[1][:-1])    
        if line_split[0] == "Test:":
            m[curr_monk]['div'] = int(line_split[-1])
        if line_split[1] == "true:":
            m[curr_monk]['m1'] = int(line_split[-1])
        if line_split[1] == "false:":
            m[curr_monk]['m0'] = int(line_split[-1])

mnum = curr_monk + 1
com_div = 1

for i in range(mnum):
    m[i]['cnt'] = 0
    com_div *= m[i]['div']


def sim_round():
    for i in range(mnum):
        items = m[i]['itm']
        fun = m[i]['op']
        div = m[i]['div']
        i0 = m[i]['m0']
        i1 = m[i]['m1']
        while items != []:
            items[0] = fun(items[0]) % com_div
            if items[0] % div == 0:
                m[i1]['itm'] += [items[0]]
            else:
                m[i0]['itm'] += [items[0]]
            del items[0]
            m[i]['cnt'] += 1
    return


for i in range(10000):
    if i % 200 == 0 and i > 0:
        print(i)
    sim_round()

busi = []

for i in range(mnum):
    busi += [m[i]['cnt']]

busi.sort()
print(busi[-1]*busi[-2])
