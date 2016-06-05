#!/usr/bin/env python3

###
# Day 18 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import copy


def neighbours(lines, row, col, max_rows, max_cols):
    total = 0
    for i in range(max(row - 1, 0), min(row + 2, max_rows)):
        for j in range(max(col - 1, 0), min(col + 2, max_cols)):
            if i != row or j != col:
                total += 1 if lines[i][j] == '#' else 0
    return total
            

def sim_game_of_life(lines):
    new_lines = []
    max_rows, max_cols = len(lines), len(lines[0])
    for row, line in enumerate(lines):
        new_line_chars = []
        for col, char in enumerate(line): 
            n = neighbours(lines, row, col, max_rows, max_cols)
            if char == '#': 
                new_line_chars.append('#' if n in (2, 3) else '.')
            else:
                new_line_chars.append('#' if n == 3 else '.')
        new_lines.append(''.join(new_line_chars))
    return new_lines


def part_one(lines):
    '''
    After the million lights incident, the fire code has gotten stricter: now,
    at most ten thousand lights are allowed. You arrange them in a 100x100
    grid.

    Never one to let you down, Santa again mails you instructions on the ideal
    lighting configuration. With so few lights, he says, you'll have to resort
    to animation.

    Start by setting your lights to the included initial configuration (your
    puzzle input). A # means "on", and a . means "off".

    Then, animate your grid in steps, where each step decides the next
    configuration based on the current one. Each light's next state (either on
    or off) depends on its current state and the current states of the eight
    lights adjacent to it (including diagonals). Lights on the edge of the grid
    might have fewer than eight neighbors; the missing ones always count as
    "off".

    The state a light should have next is based on its current state (on or
    off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off
    otherwise.  A light which is off turns on if exactly 3 neighbors are on,
    and stays off otherwise.  All of the lights update simultaneously; they all
    consider the same current state before moving to the next.

    In your grid of 100x100 lights, given your initial configuration, how many
    lights are on after 100 steps?
    '''
    for i in range(100):
        lines = sim_game_of_life(lines)
    return sum(line.count('#') for line in lines)


def mark_corners_on(lines):
    lines[0] = '#' +lines[0][1:-1] + '#'
    lines[-1] = '#' +lines[-1][1:-1] + '#'


def part_two(lines):
    '''
    You flip the instructions over; Santa goes on to point out that this is all
    just an implementation of Conway's Game of Life. At least, it was, until
    you notice that something's wrong with the grid of lights you bought: four
    lights, one in each corner, are stuck on and can't be turned off.

    In your grid of 100x100 lights, given your initial configuration, but with
    the four corners always in the on state, how many lights are on after 100
    steps?
    '''
    for i in range(100):
        mark_corners_on(lines)
        lines = sim_game_of_life(lines)
    mark_corners_on(lines)
    return sum(line.count('#') for line in lines)


def main():
    step = sim_game_of_life([
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ])
    assert step == [
        '..##..',
        '..##.#',
        '...##.',
        '......',
        '#.....',
        '#.##..',
    ]
    for i in range(3):
        step = sim_game_of_life(step)
    assert step == [
        '......',
        '......',
        '..##..',
        '..##..',
        '......',
        '......',
    ]

    step = sim_game_of_life([
        '##.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####.#',
    ])
    mark_corners_on(step)
    assert step == [
        '#.##.#',
        '####.#',
        '...##.',
        '......',
        '#...#.',
        '#.####',
    ]
    for i in range(4):
        mark_corners_on(step)
        step = sim_game_of_life(step)
    mark_corners_on(step)
    assert step == [
        '##.###',
        '.##..#',
        '.##...',
        '.##...',
        '#.#...',
        '##...#',
    ]
    with open('input/day18.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))

if __name__ == '__main__':
    main()

