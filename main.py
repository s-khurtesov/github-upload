#!/usr/bin/env

from time import time


with open(r'./data.txt', 'w') as f:
    f.write(str(time()))

with open(r'./data.txt') as f:
    print('Data:', f.read())

with open(r'./cell.png', 'rb') as f:
    png = f.read()

print(type(png), len(png), '\nSet:', set(png))

print('Nice project though!')

