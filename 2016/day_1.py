#!/usr/bin/env python


from pprint import pprint
import sys


def get_input(input_file):
    with open(input_file) as f:
        for inst in f.read().split(','):
            inst = inst.strip()
            yield (inst[0], int(inst[1:]))


def get_distance(instructions):
    directions = ['N', 'E', 'S', 'W']
    current_direction = 0
    distances = {d: 0 for d in directions}

    for direction, steps in instructions:
        if direction == 'R':
            current_direction += 1
        elif direction == 'L':
            current_direction -= 1
        current_direction %= len(directions)
        distances[directions[current_direction]] += steps

    return abs(distances['N'] - distances['S']) + abs(distances['E'] - distances['W'])
    

if __name__ == '__main__':
    print(get_distance(get_input(sys.argv[1])))

