#!/usr/bin/env python3

###
# Day 13 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

from collections import defaultdict
import itertools


def update(line, happiness, people):
    t = line.strip().rstrip('.').split()
    person, _would, effect, num, _happiness, units, _by, _sitting, _next, _to, other_person = t
    pair = person, other_person
    happiness[frozenset(pair)] += int(num) * ({'gain': 1, 'lose': -1}[effect])
    people.update(pair)


def total(happiness, people):
    for perm in itertools.permutations(people):
        yield sum(happiness[frozenset(pair)] for pair in zip(perm, perm[1:] + (perm[0],)))

    
def part_one(happiness, people):
    '''
    In years past, the holiday feast with your family hasn't gone so well. Not
    everyone gets along! This year, you resolve, will be different. You're
    going to find the optimal seating arrangement and avoid all those awkward
    conversations.

    You start by writing up a list of everyone invited and the amount their
    happiness would increase or decrease if they were to find themselves
    sitting next to each other person. You have a circular table that will be
    just big enough to fit everyone comfortably, and so each person will have
    exactly two neighbors.

    What is the total change in happiness for the optimal seating arrangement
    of the actual guest list?
    '''
    return max(total(happiness, people))


def part_two(happiness, people):
    '''
    In all the commotion, you realize that you forgot to seat yourself. At this
    point, you're pretty apathetic toward the whole thing, and your happiness
    wouldn't really go up or down regardless of who you sit next to. You assume
    everyone else would be just as ambivalent about sitting next to you, too.

    So, add yourself to the list, and give all happiness relationships that
    involve you a score of 0.

    What is the total change in happiness for the optimal seating arrangement
    that actually includes yourself?
    '''
    for p in people:
        happiness[frozenset(('myself', p))] = 0
    people.add('myself')
    return max(total(happiness, people))
    

def main():
    happiness = defaultdict(int)
    people = set()
    with open('input/day13.txt') as f:
        for line in f:
            update(line, happiness, people)
    print(part_one(happiness, people))
    print(part_two(happiness, people))


if __name__ == '__main__':
    main()

