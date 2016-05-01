#!/usr/bin/env python3

###
# Day 9 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import itertools
from collections import defaultdict


def distances(lines):
    dist = defaultdict(lambda: float('inf'))
    cities = set()
    for line in lines:
        src, arrow, dest, eq, distance = line.split()
        dist[frozenset((src, dest))] = int(distance)
        cities.update((src, dest))
    for perm in itertools.permutations(cities):
        yield sum(dist[frozenset(pair)] for pair in zip(perm, perm[1:]))


def part_one(lines):
    '''
    Every year, Santa manages to deliver all of his presents in a single night.

    This year, however, he has some new locations to visit; his elves have
    provided him the distances between every pair of locations. He can start
    and end at any two (different) locations he wants, but he must visit each
    location exactly once. What is the shortest distance he can travel to
    achieve this?
    '''
    return min(distances(lines))


def part_two(lines):
    '''
    The next year, just to show off, Santa decides to take the route with the
    longest distance instead.

    He can still start and end at any two (different) locations he wants, and
    he still must visit each location exactly once.

    For example, given the distances above, the longest route would be 982 via
    (for example) Dublin -> London -> Belfast.

    What is the distance of the longest route?
    '''
    return max(distances(lines))


def main():
    example = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]
    assert part_one(example) == 605
    assert part_two(example) == 982

    with open('input/day09.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()

