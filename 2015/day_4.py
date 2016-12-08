#!/usr/bin/env python

import hashlib
import sys

def first_five_zeroes(filepath):
    key = open(filepath).read().strip()

    i, m = -1, 'xxxxx'
    while m[:6] != '000000':
        i += 1
        k = '{}{}'.format(key, i)
        m = str(hashlib.md5(k.encode('utf-8')).hexdigest())

    print(m)
    return i

if __name__ == '__main__':
    filepaths = ['day_4_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        print(first_five_zeroes(filepath))