import io
import sys
import math


f = open("input.in", "r", encoding='utf-8')
reading = True

p = 14


def detect(str):
    strlen = len(str)-3
    for i in range(strlen):
        if len(set(str[i:i+p])) == p:
            return i + p
    return -1


while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    print(detect(line))
