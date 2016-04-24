#!/usr/bin/env python

###
# Day 1 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

def part_one(s):
    '''
    Santa is trying to deliver presents in a large apartment building, but he
    can't find the right floor - the directions he got are a little confusing.
    He starts on the ground floor (floor 0) and then follows the instructions
    one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing
    parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he will
    never find the top or bottom floors.
    
    To what floor do the instructions take Santa?
    '''
    return sum(1 if c == '(' else -1 for c in s)

def part_two(s):
    '''
    Now, given the same instructions, find the position of the first character
    that causes him to enter the basement (floor -1). The first character in
    the instructions has position 1, the second character has position 2, and
    so on.

    What is the position of the character that causes Santa to first enter the
    basement?
    '''
    floor = 0
    for i, c in enumerate(s, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i


def main():
    assert part_one('(())') == 0
    assert part_one('()()') == 0
    assert part_one('(((') == 3
    assert part_one('(()(()(') == 3
    assert part_one('))(((((') == 3
    assert part_one('())') == -1
    assert part_one('))(') -1
    assert part_one(')))') == -3
    assert part_one(')())())') == -3

    assert part_two(')') == 1
    assert part_two('()())') == 5

    with open('input/day01.txt') as f:
        s = f.read().strip()

    print(part_one(s))
    print(part_two(s))

if __name__ == '__main__':
    main()
