#!/usr/bin/env python

import re
import sys

regex = re.compile(r'(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)')

def on_count(filepath):
    data = open(filepath).read()
    grid = [[False]*1000 for i in range(1000)]

    for line in data.splitlines():
        match = regex.search(line)
        cmd = match.group(1)
        x_0, y_0 = [int(x) for x in match.group(2).split(',')]
        x_1, y_1 = [int(x) for x in match.group(3).split(',')]

        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                if cmd == 'turn on':
                    grid[x][y] = True
                elif cmd == 'turn off':
                    grid[x][y] = False
                elif cmd == 'toggle':
                    grid[x][y] = not grid[x][y]

    on = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y]: on += 1

    return on


def brightness_level(filepath):
    data = open(filepath).read()
    grid = [[0]*1000 for i in range(1000)]

    for line in data.splitlines():
        match = regex.search(line)
        cmd = match.group(1)
        x_0, y_0 = [int(x) for x in match.group(2).split(',')]
        x_1, y_1 = [int(x) for x in match.group(3).split(',')]

        for x in range(x_0, x_1 + 1):
            for y in range(y_0, y_1 + 1):
                if cmd == 'turn on':
                    grid[x][y] += 1
                elif cmd == 'turn off':
                    if grid[x][y] > 0: grid[x][y] -= 1
                elif cmd == 'toggle':
                    grid[x][y] += 2

    brightness = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            brightness += grid[x][y]

    return brightness

if __name__ == '__main__':
    filepaths = ['day_6_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        # print(on_count(filepath))
        print(brightness_level(filepath))