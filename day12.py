#!/usr/bin/env python3

###
# Day 12 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import json

class NoValue(object): pass

def sum_nums(obj, ignore=NoValue):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_nums(elt, ignore) for elt in obj) 
    elif isinstance(obj, dict):
        values = obj.values()
        if ignore is NoValue or ignore not in values:
            return sum(sum_nums(elt, ignore) for elt in values)
    return 0


def part_one(obj):
    '''
    Santa's Accounting-Elves need help balancing the books after a recent
    order. Unfortunately, their accounting software uses a peculiar storage
    format. That's where you come in.

    They have a JSON document which contains a variety of things: arrays
    ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job
    is to simply find all of the numbers throughout the document and add them
    together.

    What is the sum of all numbers in the document?
    '''
    return sum_nums(obj)


def part_two(obj):
    '''
    Uh oh - the Accounting-Elves have realized that they double-counted
    everything red.

    Ignore any object (and all of its children) which has any property with the
    value "red". Do this only for objects ({...}), not arrays ([...]).
    '''
    return sum_nums(obj, ignore='red')


def main():
    assert sum_nums([1,2,3]) == 6
    assert sum_nums({"a":2,"b":4}) == 6
    assert sum_nums([[[3]]]) == 3
    assert sum_nums({"a":{"b":4},"c":-1}) == 3
    assert sum_nums({"a":[-1,1]}) == 0
    assert sum_nums([-1,{"a":1}]) == 0
    assert sum_nums([]) == 0
    assert sum_nums({}) == 0
    assert sum_nums('abc') == 0
    assert sum_nums({'a': 'abc'}) == 0
    assert sum_nums([1,2,3], ignore='red') == 6
    assert sum_nums([1,{"c":"red","b":2},3], ignore='red') == 4
    assert sum_nums({"d":"red","e":[1,2,3,4],"f":5}, ignore='red') == 0
    assert sum_nums([1,"red",5], ignore='red') == 6
    obj = json.load(open('input/day12.txt'))
    print(part_one(obj))
    print(part_two(obj))


if __name__ == '__main__':
    main()

