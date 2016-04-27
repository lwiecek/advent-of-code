#!/usr/bin/env python3

###
# Day 6 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import itertools
from collections import defaultdict


def get_min_max(fragments):
    return tuple(int(v) for v in (fragments[0] + ',' + fragments[2]).split(','))


def walk(min_x, min_y, max_x, max_y, func):
    for coord in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        func(coord)


def update(line, turn_on, turn_off, toggle):
    fragments = line.split()
    if line.startswith('turn on'):
        walk(*get_min_max(fragments[2:]), func=turn_on)
    elif line.startswith('turn off'):
        walk(*get_min_max(fragments[2:]), func=turn_off)
    elif line.startswith('toggle'):
        walk(*get_min_max(fragments[1:]), func=toggle)


def part_one(lines):
    '''
    Because your neighbors keep defeating you in the holiday house decorating
    contest year after year, you've decided to deploy one million lights in a
    1000x1000 grid.

    Furthermore, because you've been especially nice this year, Santa has
    mailed you instructions on how to display the ideal lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; the
    lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
    instructions include whether to turn on, turn off, or toggle various
    inclusive ranges given as coordinate pairs. Each coordinate pair represents
    opposite corners of a rectangle, inclusive; a coordinate pair like 0,0
    through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all
    start turned off.

    To defeat your neighbors this year, all you have to do is set up your
    lights by doing the instructions Santa sent you in order.

    After following the instructions, how many lights are lit?
    '''
    on = set()
    def toggle(c):
        if c in on:
            on.remove(c)
        else:
            on.add(c)

    for line in lines:
        update(line, on.add, on.discard, toggle)

    return len(on)


def part_two(lines):
    '''
    You just finish implementing your winning light pattern when you realize
    you mistranslated Santa's message from Ancient Nordic Elvish.

    The light grid you bought actually has individual brightness controls; each
    light can have a brightness of zero or more. The lights all start at zero.

    The phrase turn on actually means that you should increase the brightness
    of those lights by 1.

    The phrase turn off actually means that you should decrease the brightness
    of those lights by 1, to a minimum of zero.

    The phrase toggle actually means that you should increase the brightness of
    those lights by 2.

    What is the total brightness of all lights combined after following Santa's
    instructions?
    '''
    brightness = defaultdict(int)
    def turn_on(c):
        brightness[c] += 1

    def turn_off(c):
        brightness[c] = max(brightness[c] - 1, 0)
        
    def toggle(c):
        brightness[c] += 2

    for line in lines:
        update(line, turn_on, turn_off, toggle)

    return sum(brightness.values())


def main():
    with open('input/day06.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()
