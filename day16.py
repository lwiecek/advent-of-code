#!/usr/bin/env python3

###
# Day 16 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import re

FACTS = {
    ('children', 3),
    ('cats', 7),
    ('samoyeds', 2),
    ('pomeranians', 3),
    ('akitas', 0),
    ('vizslas', 0),
    ('goldfish', 5),
    ('trees', 3),
    ('cars', 2),
    ('perfumes', 1),
}


def get_known(line):
    return {(key, int(value)) for key, value in re.findall(r'(\w+): (\d+)', line)}


def part_one(lines):
    '''
    Your Aunt Sue has given you a wonderful gift, and you'd like to send her a
    thank you card. However, there's a small problem: she signed it "From, Aunt
    Sue".

    You have 500 Aunts named "Sue".

    So, to avoid sending the card to the wrong person, you need to figure out
    which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave
    you the gift. You open the present and, as luck would have it, good ol'
    Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you
    wanted. Or needed, as the case may be.

    The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a
    few specific compounds in a given sample, as well as how many distinct
    kinds of those compounds there are. According to the instructions, these
    are what the MFCSAM can detect:

    - children, by human DNA age analysis.
    - cats. It doesn't differentiate individual breeds.
    - Several seemingly random breeds of dog: samoyeds, pomeranians, akitas,
      and vizslas.
    - goldfish. No other kinds of fish.
    - trees, all in one group.
    - cars, presumably by exhaust or gasoline or something.
    - perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

    You make a list of the things you can remember about each Aunt Sue. Things
    missing from your list aren't zero - you simply don't remember the value.

    What is the number of the Sue that got you the gift?
    '''
    for i, line in enumerate(lines, 1):
        if get_known(line).issubset(FACTS):
            return i
    return None


def part_two(lines):
    '''
    As you're about to send the thank you note, something in the MFCSAM's
    instructions catches your eye. Apparently, it has an outdated
    retroencabulator, and so the output from the machine isn't exact values -
    some of them indicate ranges.

    In particular, the cats and trees readings indicates that there are greater
    than that many (due to the unpredictable nuclear decay of cat dander and
    tree pollen), while the pomeranians and goldfish readings indicate that
    there are fewer than that many (due to the modial interaction of
    magnetoreluctance).

    What is the number of the real Aunt Sue?
    '''
    greater_than = {'cats', 'trees'}
    fewer_than = {'pomeranians', 'goldfish'}
    facts = dict(FACTS)
    for i, line in enumerate(lines, 1):
        ok = True
        for key, value in get_known(line):
            ok = ok and (value > facts[key] if key in greater_than else True)
            ok = ok and (value < facts[key] if key in fewer_than else True)
            ok = ok and (value == facts[key] if key not in greater_than|fewer_than else True)
        if ok:
            return i
    return None


def main():
    with open('input/day16.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()

