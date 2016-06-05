#!/usr/bin/env python3

###
# Day 11 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import re
from string import ascii_lowercase as letters


TRIPLES = [''.join(t) for t in zip(letters, letters[1:], letters[2:])]


def meets_requirements(pwd):
    if not any(t in pwd for t in TRIPLES):
        return False
    if set('oil') & set(pwd):
        return False
    if not re.match(r'.*(.)\1.*(.)\2.*', pwd):
        return False
    return True


def incremented(pwd):
    group = re.search('z*.', pwd[::-1]).group(0)
    same = pwd[:-len(group)]
    incr_char = chr(ord(group[-1]) + 1) if group[-1] < 'z' else 'aa'
    updated = incr_char + (len(group) - 1) * 'a'
    return same + updated


def next_password(pwd):
    pwd = incremented(pwd)
    while not meets_requirements(pwd):
        pwd = incremented(pwd)
    return pwd


def part_one(puzzle_input):
    '''
    Santa's previous password expired, and he needs help choosing a new one.

    To help him remember his new password after the old one expires, Santa has
    devised a method of coming up with a password based on the previous one.
    Corporate policy dictates that passwords must be exactly eight lowercase
    letters (for security reasons), so he finds his new password by
    incrementing his old password string repeatedly until it is valid.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so
    on. Increase the rightmost letter one step; if it was z, it wraps around to
    a, and repeat with the next letter to the left until one doesn't wrap
    around.

    Given Santa's current password (your puzzle input), what should his next
    password be?
    '''
    return next_password(puzzle_input)


def part_two(puzzle_input):
    '''
    Santa's password expired again. What's the next one?
    '''
    return next_password(puzzle_input)


def main():
    assert incremented('a') == 'b'
    assert incremented('xx') == 'xy'
    assert incremented('zzz') == 'aaaa'
    assert not meets_requirements('hijklmmn')
    assert not meets_requirements('abbceffg')
    assert not meets_requirements('abbcegjk')
    assert meets_requirements('abcdffaa')
    assert meets_requirements('ghjaabcc')
    assert not meets_requirements('aaa')
    puzzle_input = 'hepxcrrq'
    part_one_password = part_one(puzzle_input)
    print(part_one_password)
    print(part_two(part_one_password))


if __name__ == '__main__':
    main()
