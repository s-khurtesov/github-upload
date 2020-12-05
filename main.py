#!/usr/bin/env

from time import time


with open(r'./data.bin', 'w') as f:
    f.write(str(time()))

with open(r'./data.bin') as f:
    print('Data:', f.read())

print('Nice project though!')

