#!/usr/bin/env python3

###
# Day 15 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import re


def choose(parameters, amounts, teaspoons, calories):
    if len(amounts) == len(parameters):
        if teaspoons:
            return 0
        result = 1
        last = len(parameters[0]) - 1
        for i, p in enumerate(zip(*parameters)): 
            value = sum(a * px for a, px in zip(amounts, p))
            if i == last:
                if value != calories:
                    return 0
            elif value <= 0:
                return 0
            else:
                result *= value
        return result

    return max(
        choose(parameters, amounts + (i,), teaspoons - i, calories) for i in range(teaspoons + 1)
    )

        
def get_parameters(line):
    return [int(num) for num in re.findall(r"[\d-]+", line)]


def part_one(lines):
    '''
    Today, you set out on the task of perfecting your milk-dunking cookie
    recipe. All you have to do is find the right balance of ingredients.

    Your recipe leaves room for exactly 100 teaspoons of ingredients. You make
    a list of the remaining ingredients you could use to finish the recipe
    (your puzzle input) and their properties per teaspoon:

    - capacity (how well it helps the cookie absorb milk)
    - durability (how well it keeps the cookie intact when full of milk)
    - flavor (how tasty it makes the cookie)
    - texture (how it improves the feel of the cookie)
    - calories (how many calories it adds to the cookie)

    You can only measure ingredients in whole-teaspoon amounts accurately, and
    you have to be accurate so you can reproduce your results in the future.
    The total score of a cookie can be found by adding up each of the
    properties (negative totals become 0) and then multiplying together
    everything except calories.  

    Given the ingredients in your kitchen and their properties, what is the
    total score of the highest-scoring cookie you can make?  
    '''
    parameters = [get_parameters(line)[:-1] + [0] for line in lines]
    return choose(parameters, (), 100, 0)


def part_two(lines):
    '''
    Your cookie recipe becomes wildly popular! Someone asks if you can make
    another recipe that has exactly 500 calories per cookie (so they can use it
    as a meal replacement). Keep the rest of your award-winning process the
    same (100 teaspoons, same ingredients, same scoring system).
    
    Given the ingredients in your kitchen and their properties, what is the
    total score of the highest-scoring cookie you can make with a calorie total
    of 500?
    ''' 
    parameters = [get_parameters(line) for line in lines]
    return choose(parameters, (), 100, 500)
    
    return


def main():
    example = [
        'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
    ]
    assert part_one(example) == 62842880
    assert part_two(example) == 57600000

    with open('input/day15.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()

