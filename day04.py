#!/usr/bin/env python3

###
# Day 4 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import hashlib

def mine(key, zeros):
    i = 1
    while not hashlib.md5((key + str(i)).encode()).hexdigest().startswith('0' * zeros):
        i += 1
    return i


def part_one(key):
    '''
    Santa needs help mining some AdventCoins (very similar to bitcoins) to use
    as gifts for all the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with
    at least five zeroes. The input to the MD5 hash is some secret key (your
    puzzle input, given below) followed by a number in decimal. To mine
    AdventCoins, you must find Santa the lowest positive number (no leading
    zeroes: 1, 2, 3, ...) that produces such a hash.
    '''
    return mine(key, 5)


def part_two(key):
    '''
    Now find one that starts with six zeroes.
    '''
    return mine(key, 6)


def main():
    assert part_one('abcdef') == 609043
    assert part_one('pqrstuv') == 1048970

    key = 'bgvyzdsv'

    print(part_one(key))
    print(part_two(key))


if __name__ == '__main__':
    main()

