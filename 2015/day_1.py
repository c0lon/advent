#!/usr/bin/env python

import sys

def read_instructions(filepath):
    floor, seen_basement = 0, False
    for i, char in enumerate(open(filepath).read()):
        if char == '(': floor += 1
        elif char == ')': floor -= 1

        if floor < 0 and not seen_basement:
            print(i+1)
            seen_basement = True

    return floor


if __name__ == '__main__':
    filepaths = ['day_1_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        print(read_instructions(filepath))