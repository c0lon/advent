#!/usr/bin/env python

import sys

def presents(filepath):
    santa = {'x': 0, 'y': 0}
    robo = {'x': 0, 'y': 0}
    actor = santa
    visited = []

    moves = open(filepath).read()
    for i, move in enumerate(moves):
        current = (actor['x'], actor['y'])
        if current not in visited:
            visited.append(current)

        if not i % 2:
            actor = santa
        else:
            actor = robo

        if move == '^':
            actor['y'] += 1
        elif move == '>':
            actor['x'] += 1
        elif move == 'v':
            actor['y'] -= 1
        elif move == '<':
            actor['x'] -= 1

    return len(visited)

if __name__ == '__main__':
    filepaths = ['day_3_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        print(presents(filepath))