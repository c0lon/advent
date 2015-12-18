#!/usr/bin/env python

import re
import sys

def wrapping_supplies(filepath):
    paper, ribbon = 0, 0

    data = open(filepath).read()
    regex = re.compile('(\d+)x(\d+)x(\d+)')
    for match in regex.finditer(data):
        l, w, h = sorted([int(d) for d in match.groups()])
        faces = [l*w, l*h, w*h]
        paper += 2*sum(faces) + min(faces)

        ribbon += 2*l + 2*w + l*w*h

    return paper, ribbon

if __name__ == '__main__':
    filepaths = ['day_2_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        print(wrapping_supplies(filepath))