#!/usr/bin/env python

import sys

def nice_strings(filepath):
    data = open(filepath).read()

    vowels = ['a', 'e', 'i', 'o', 'u']
    not_allowed = ['ab', 'cd', 'pq', 'xy']

    nice = 0

    for line in data.splitlines():
        vowel_count = 0
        old_char, double = '', False

        allowed = True
        for char in line:
            if old_char + char in not_allowed:
                allowed = False
                break

            if old_char == char:
                double = True

            if char in vowels:
                vowel_count += 1

            old_char = char

        if allowed and double and vowel_count >= 3:
            nice += 1

    return nice

if __name__ == '__main__':
    filepaths = ['day_5_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        print(nice_strings(filepath))