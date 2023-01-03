import io
import sys
import math


std_alt = {4: '2', 3: '1', 2: '0', 1: '-', 0: '='}
std = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def snafu_to_dec(snaf):
    dsum = 0
    p = len(snaf) - 1
    for s in snaf:
        dsum += std[s]*(5**p)
        p -= 1
    return dsum


def dec_to_snafu(dec):
    p, psum = 0, 0 
    dec_alt = dec
    while psum < dec:
        psum += 2*(5**p)
        p += 1
    for i in range(p):
        dec_alt += (5**i)*2
    digits = ''
    for i in range(p):
        pow = p-1-i
        d = dec_alt // 5**pow
        dec_alt = dec_alt - d*(5**pow)
        digits += std_alt[d]
    return digits


f = open("input.in", "r", encoding='utf-8')
reading = True
fuel_sum = 0

while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    fuel_sum += snafu_to_dec(line.strip())

print(dec_to_snafu(fuel_sum))
