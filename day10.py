#!/usr/bin/env python3

###
# Day 10 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import itertools

def look_and_say(s):
    count = 1
    result = []
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            result.append('{}{}'.format(count, prev))
            count = 1
            prev = c
    result.append('{}{}'.format(count, prev))
    return ''.join(result)


def solve(puzzle_input, iterations):
    for i in range(iterations): 
        puzzle_input = look_and_say(puzzle_input)
    return len(puzzle_input)
        
def part_one(puzzle_input):
    '''
    Today, the Elves are playing a game called look-and-say. They take turns
    making sequences by reading aloud the previous sequence and using that
    reading as the next sequence. For example, 211 is read as "one two, two
    ones", which becomes 1221 (1 2, 2 1s).

    Look-and-say sequences are generated iteratively, using the previous value
    as input for the next step. For each step, take the previous value, and
    replace each run of digits (like 111) with the number of digits (3)
    followed by the digit itself (1).

    Starting with the digits in your puzzle input, apply this process 40 times.
    What is the length of the result?
    '''
    return solve(puzzle_input, 40)


def part_two(puzzle_input):
    '''
    Neat, right? You might also enjoy hearing John Conway talking about this
    sequence (that's Conway of Conway's Game of Life fame).

    Now, starting again with the digits in your puzzle input, apply this
    process 50 times. What is the length of the new result?
    '''
    return solve(puzzle_input, 50)


def main():
    assert look_and_say('1') == '11'
    assert look_and_say('11') == '21'
    assert look_and_say('21') == '1211'
    assert look_and_say('1211') == '111221'
    assert look_and_say('111221') == '312211'

    puzzle_input = '1113122113'
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == '__main__':
    main()

