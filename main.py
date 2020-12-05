#!/usr/bin/env

from time import time


with open(r'./data.txt', 'w') as f:
    f.write(str(time()))

with open(r'./data.txt') as f:
    print('Data:', f.read())

print('Nice project though!')

