#!/usr/bin/env python3

###
# Day 5 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

from collections import Counter


def part_one(lines):
    '''
    Santa needs help figuring out which strings in his text file are naughty or
    nice.

    A nice string is one with all of the following properties:

    - It contains at least three vowels (aeiou only), like aei, xazegov, or
    aeiouaeiouaeiou.

    - It contains at least one letter that appears twice in a row, like xx,
    abcdde (dd), or aabbccdd (aa, bb, cc, or dd). 
    
    - It does not contain the strings ab, cd, pq, or xy, even if they are part
    of one of the other requirements.
    '''

    VOWELS = 'aeiou'
    FORBIDEN = {'ab', 'cd', 'pq', 'xy'}

    def is_nice(s):
        cnts = Counter(s)
        if sum(cnts[v] for v in VOWELS) < 3:
            return False
        if not any(x[0] == x[1] for x in zip(s, s[1:])):
            return False
        if any((f in s) for f in FORBIDEN):
            return False
        return True
    return sum(is_nice(line) for line in lines)


def part_two(lines):
    '''
    Realizing the error of his ways, Santa has switched to a better model of
    determining whether a string is naughty or nice. None of the old rules
    apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    - It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    aaa (aa, but it overlaps).

    - It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.
    '''

    def is_nice(s):
        if not any((''.join(pair) in s[i+2:]) for i, pair in enumerate(zip(s, s[1:]))):
            return False
        if not any (x[0] == x[1] for x in zip(s, s[2:])):
            return False
        return True

    return sum(is_nice(line) for line in lines)
    

def main():
    assert part_one(['ugknbfddgicrmopn']) == 1
    assert part_one(['aaa']) == 1
    assert part_one(['jchzalrnumimnmhp']) == 0
    assert part_one(['haegwjzuvuyypxyu']) == 0
    assert part_one(['dvszwmarrgswjxmb']) == 0
    
    assert part_two(['qjhvhtzxzqqjkmpb']) == 1
    assert part_two(['xxyxx']) == 1
    assert part_two(['uurcxstgmygtbstg']) == 0
    assert part_two(['ieodomkazucvgmuy']) == 0
    
    with open('input/day05.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()

