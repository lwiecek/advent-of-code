#!/usr/bin/env python3

###
# Day 17 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import copy
         

def solve(litres, lines):
    sizes = [int(val) for val in lines]
    ways = {}
    for i in range(0, 2**len(sizes)):
        total, bits = 0, 0
        for j, s in enumerate(sizes):
            if (i >> j) & 1:
                total += s
                bits += 1
            if total > litres:
                break
        if total == litres:
            ways[bits] = ways.get(bits, 0) + 1
    return ways


def part_one(solution):
    '''
    The elves bought too much eggnog again - 150 liters this time. To fit it
    all into your refrigerator, you'll need to move it into smaller containers.
    You take an inventory of the capacities of the available containers.
    
    Filling all containers entirely, how many different combinations of
    containers can exactly fit all 150 liters of eggnog?
    '''
    return sum(solution.values())


def part_two(solution):
    '''
    While playing with all the containers in the kitchen, another load of
    eggnog arrives! The shipping and receiving department is requesting as many
    containers as you can spare.

    Find the minimum number of containers that can exactly fit all 150 liters
    of eggnog. How many different ways can you fill that number of containers
    and still hold exactly 150 litres?
    '''
    return solution[min(solution)]


def main():
    example = [20, 15, 10, 5, 5]
    solution = solve(25, example)
    assert part_one(solution) == 4
    assert part_two(solution) == 3
    with open('input/day17.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    solution = solve(150, lines)
    print(part_one(solution))
    print(part_two(solution))


if __name__ == '__main__':
    main()
